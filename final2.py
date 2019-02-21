import os
import apiclient
from apiclient import errors
from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import base64
import re
# from nltk.corpus import stopwords
import nltk
# from stop_words import get_stop_words
# from sklearn.feature_extraction.text import TfidfVectorizer
import time
# import dateutil.parser as parser
# from datetime import datetime
# import datetime
# import unicodecsv as csv
from httplib2 import Http
from oauth2client import file, client, tools
# from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as VS

def GetMessageBody(service, user_id, msg_id):
	try:
		message = service.users().messages().get(userId=user_id, id=msg_id, format='raw').execute()
		msg_str = base64.urlsafe_b64decode(message['raw'].encode('ASCII'))
		mime_msg = email.message_from_string(msg_str)
		messageMainType = mime_msg.get_content_maintype()
		# print mime_msg
		if mime_msg.is_multipart():
			# print "yes"
			for part in mime_msg.get_payload():
				if part.get_content_maintype() == 'text':
					return part.get_payload()
			return ""
		elif messageMainType == 'text':
			return mime_msg.get_payload()
	except errors.HttpError as error:
		print('An error occurred: %s' % error)

def GetThread(service, user_id, thread_id):
	try:
	  	thread = service.users().threads().get(userId=user_id, id=thread_id).execute()
	  	messages = thread['messages']
	  	num_msgs = len(messages)
	  	conversation = []
	  	msgg = thread['messages'][0]['payload']
	  	subject = ''
	  	for header in msgg['headers']:
	  		if header['name'] == 'Subject':
	  			subject = header['value']
	  		if subject == "":
	  			subject = ""
	  	customer = ''
	  	for header in msgg['headers']:
	  		if header['name'] == 'From':
	  			customer = header['value']
	  	for i in range(num_msgs):
	  		msg = messages[i]['snippet']
	  		
	  		if "@" not in msg or "glamazonunofficial@gmail.com" in msg:
	  			msg = customer + ": " + msg
	  		else:
	  			msg = "Team: " + msg
	  		msg = msg.split("On", 1)[0]
	  		conversation.append(msg)
	  	return conversation, subject
	except errors.HttpError as error:
		print('An error occurred: %s' % error)

def ListThreadsWithLabels(service, user_id, label_ids=[]):
  try:
    response = service.users().threads().list(userId=user_id,
                                              labelIds=label_ids).execute()
    threads = []
    if 'threads' in response:
      threads.extend(response['threads'])

    while 'nextPageToken' in response:
      page_token = response['nextPageToken']
      response = service.users().threads().list(userId=user_id,
                                                labelIds=label_ids,
                                                pageToken=page_token).execute()
      threads.extend(response['threads'])

    return threads
  except errors.HttpError as error:
    print('An error occurred: %s' % error)

def getscores():
	SCOPES = 'https://www.googleapis.com/auth/gmail.readonly'
	store = file.Storage('storage.json')
	creds = store.get()
	# nltk.download ('stopwords')
	# stop_words = get_stop_words('en')
	analyzer = VS()
	# stopwords_list = stopwords.words('english') + stopwords.words('portuguese')
	# tvd = TfidfVectorizer(analyzer='word',ngram_range=(1, 3),min_df=0.003,max_df=0.01,max_features=5000,norm='l1',stop_words=stopwords_list)
	if not creds or creds.invalid:
		flow = client.flow_from_clientsecrets('client_secret.json',SCOPES)
		creds = tools.run_flow(flow,store)
	GMAIL = discovery.build('gmail','v1',http=creds.authorize(Http()))

	label = 'INBOX'

	Spl_char = [",","-",".",";",">","<","=","&",":","#","!"]
	threads = ListThreadsWithLabels(GMAIL,'me',[label])
	# all_threads = []
	all = []
	for t in threads:
		conversation, subject = GetThread(GMAIL,'me',t['id'])
		score = []
		for msg in conversation:
			if "Team" not in msg:
				vs = analyzer.polarity_scores(msg)
				score.append(vs['compound'])

		one = [subject,conversation,score]
		
		all.append(one)
	return all

getscores()
