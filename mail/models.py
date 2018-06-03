from django.db import models
import json

class Thread(models.Model):
    subject = models.CharField(max_length = 140)
    messages = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.subject
    def set_messages(self,x):
    	self.messages = json.dumps(x)
    def get_messages(self):
    	return json.loads(self.messages)