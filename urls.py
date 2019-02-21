from django.conf.urls import url, include
# from django.views.generic import ListView, DetailView
# from mail.models import Thread
from .views import func,func1
urlpatterns = [ 
	 url(r'^conversation/(?P<my_id>\d+)',func1),
	url(r'^$',func),
]