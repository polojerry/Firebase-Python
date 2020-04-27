import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# initializations
cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# adding data
doc_ref = db.collection('python').document()
doc_ref.set({
    'fname': 'Jeremiah',
    'lname': 'Polo',
    'age': 24

})

# Reading the data
py_ref = db.collection('python')
docs = py_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict()))


