# Sentimenatal Inbox

## Overview
A Django based webapp that extracts Gmail threads using the Gmail API and analyses the sentiments depicted in the mailing threads using Vader Sentiment Analysis Tool. Note that, the Gmail API services of the Account must be enabled.
The front-end is made using HTML-CSS, Bootstrap and javascript and the back-end using django.



### Sample: 
This is how the Inbox will look like. The rightmost column depicts the transition of sentiments: Red shows a negative sentiment, Green shows a positive sentiment and Yellow shows a neutral sentiment.
#### Inbox
![alt text](images/Inbox.png)

When a partcular email thread is selected, the page is redirected to another page that shows the mails sent back and forth between the client and admin. Along with each message the client has sent, a sentiment score is shown. 
#### Mailing Thread
![alt text](images/Thread.png)

This analysis of emails is helpful for organisations that want to improve relationships with their customers and also prioritize different mails in their inbox. 

