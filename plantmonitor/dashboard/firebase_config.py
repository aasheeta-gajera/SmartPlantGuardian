# dashboard/firebase_config.py
import firebase_admin
from firebase_admin import credentials, db

cred = credentials.Certificate("firebase-key.json")  # Your JSON file
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://aitools-7593a-default-rtdb.firebaseio.com'
})
