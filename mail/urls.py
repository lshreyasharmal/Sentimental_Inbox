from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from mail.models import Thread
from .views import func
urlpatterns = [ 
	url(r'^inbox',func),
 # url(r'^(?P<pk>\d+)$', conv)
url(r'^$', ListView.as_view(queryset=Thread.objects.all().order_by("-date")[:25],template_name="mail/mail.html")),
                url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Thread,template_name="mail/thread.html")),
]