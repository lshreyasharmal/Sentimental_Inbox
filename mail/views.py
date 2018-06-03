from django.shortcuts import render
from django.http import HttpResponse
from .final2 import getscores
import json

def func(request):
	data = getscores()
	result =[]

	for i in range(len(data)):
		temp = []
		temp.append(i+1)
		temp.append(data[i][0])
		temp.append(data[i][2])
		result.append(temp)
	# context = {
	# "result" : result
	# }
	return render(request,'mail/inbox.html',result=json.dumps(result))


# Create your views here.
