#! python3

import firebase_admin, sys
from firebase_admin import messaging
from . import firebase_db
import datetime

class Notification:
    title = ""
    body = 0
    category = ""
    date_time = datetime.datetime.now()

    def __init__(self, title, body, category, date_time):
        self.title = title
        self.body = body
        self.category = category
        self.date_time = date_time

def send(notification: Notification):
    condition = "'all' in topics"

    message = messaging.Message(
        notification=messaging.Notification(
            title='%s' % (notification.title),
            body='%s' % (notification.body),
        ),
        condition=condition,
    )

    # Send a message to devices subscribed to the combination of topics
    # specified by the provided condition.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)

def send_and_save(notification: Notification):
    send(notification)

    data = {
        u'title': u'%s' % notification.title,
        u'body': u'%s' % notification.body,
        u'category': u'%s' % notification.category,
        u'date_time': datetime.datetime.now()
    }
    firebase_db.write('notifications', data)



