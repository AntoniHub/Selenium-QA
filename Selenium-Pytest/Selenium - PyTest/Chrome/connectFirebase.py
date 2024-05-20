import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

result = db.collection('clients').document('3hqrdVOkcpXcnYoZjaB9').get()
if result.exists:
    print(result.to_dict())