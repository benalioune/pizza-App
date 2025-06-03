import firebase_admin
from firebase_admin import credentials
import json
import pyrebase
import os

# Load configurations from JSON files
with open('configs/firebase_config.json', 'r') as config_file:
    firebase_config_json = json.load(config_file)

with open('configs/firebase_service_account.json', 'r') as key_file:
    service_account_key_json = json.load(key_file)

# Initialize the app with a service account
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_key_json)
    firebase_admin.initialize_app(cred)

# Initialize Firebase with configuration
firebase = pyrebase.initialize_app(firebase_config_json)
# Get database and auth instances
db = firebase.database()
authTodo = firebase.auth()


