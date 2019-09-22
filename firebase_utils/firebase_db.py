#! python3

import firebase_admin, sys
from firebase_admin import messaging, firestore

def read(collection_name):
    db = firestore.client()
    users_ref = db.collection(u'%s' % collection_name)
    docs = users_ref.stream()
    return docs
    
def write(collection_name, data):
    db = firestore.client()

    db.collection(u'%s' % collection_name).add(data)