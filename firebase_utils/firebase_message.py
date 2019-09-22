#! python3

import firebase_admin, sys
from firebase_admin import messaging
from . import firebase_db
import datetime
from multipledispatch import dispatch

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

@dispatch(str, str, str)
def send(the_title, the_body, topic):
    # send the message only to devices subscribed to this topic
    condition = "'%s' in topics" % topic

    message = messaging.Message(
        notification=messaging.Notification(
            title='%s' % (the_title),
            body='%s' % (the_body),
        ),
        condition=condition,
    )

    # Send a message to devices subscribed to the topic
    response = messaging.send(message)
    print('Successfully sent message:', response)

@dispatch(str, str)
def send(the_title, the_body):
    # you must have a topic defined in your Firebase console called "all"
    # your device must be subscribed to the topic "all"
    send(the_title, the_body, 'all')

@dispatch(Notification)
def send(notification: Notification):
    send(notification.title, notification.body)

# send a push notification and store the contents in a collection called 'notifications'
def send_and_save(notification: Notification):
    send(notification)

    data = {
        u'title': u'%s' % notification.title,
        u'body': u'%s' % notification.body,
        u'category': u'%s' % notification.category,
        u'date_time': datetime.datetime.now()
    }
    firebase_db.write('notifications', data)



