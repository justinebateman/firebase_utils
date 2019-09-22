#! python3

import firebase_admin, sys
from firebase_admin import messaging

def send_firebase(the_title, the_body):
    condition = "'all' in topics"

    message = messaging.Message(
        notification=messaging.Notification(
            title='%s' % (the_title),
            body='%s' % (the_body),
        ),
        condition=condition,
    )

    # Send a message to devices subscribed to the combination of topics
    # specified by the provided condition.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)