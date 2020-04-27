from firebase_admin import firestore
import firebase_initializer

# Initialize Firebase
firebase_initializer.initialize()

# firestore client
db = firestore.client()

# adding data
doc_ref = db.collection('python').document()
doc_ref.set({
    'name': 'Python 3.0',
    'code': '3.0',
    'year_launched': 2012

})

# Reading the data
py_ref = db.collection('python')
docs = py_ref.stream()

for doc in docs:
    print('{} => {} '.format(doc.id, doc.to_dict()))
