from django.shortcuts import render
from django.http import HttpResponse
from .final2 import getscores
import json

def func(request):
	data = getscores()
	result = []
	for i in range(len(data)):
		temp = {}
		temp['subject'] = data[i][0]
		temp['scores'] = data[i][2]
		result.append(temp)
	context = {
	"result" : result,
	}
	return render(request,'mail/inbox.html',context)



def func1(request,my_id):
	# id_ = request.GET.get(id=)

	my_id = int(my_id)
	data = getscores()
	final = []
	for i in range(len(data)):
		if i == my_id-1:
			j = 0
			for msg in data[i][1]:
				temp = {}
				temp['msg'] = msg
				if "Team" in msg:
					temp['score']= ""
				else:
					temp['score']= (data[i][2][j])
					j+=1
				final.append(temp)
			break	


	# 	score = data[i][2]
	# 	convs = data[i][1]
	# 	j = 0
	# 	temp2 = []
	# 	for k in convs:
	# 		temp = []
	# 		if "Team" in k:
	# 			temp.append(k)
	# 			temp.append("")
	# 		else:
	# 			temp.append(k)
	# 			temp.append(score[j])
	# 			j+=1
	# 		temp2.append(temp)
	# 	final.append(temp2)
	# print(final)

	context = {
	"final" : final,
	}
	return render(request,'mail/conversation.html',context)