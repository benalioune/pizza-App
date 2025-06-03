import firebase_admin
from firebase_admin import credentials
import json
import pyrebase
import os
from dotenv import load_dotenv

load_dotenv()

def get_firebase_config():
    """Get Firebase configuration from file or environment variables"""
    try:
        # Try to load from file first
        with open('configs/firebase_config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        # If file not found, try environment variables
        required_keys = [
            "apiKey", "authDomain", "databaseURL", "projectId",
            "storageBucket", "messagingSenderId", "appId"
        ]
        config = {}
        for key in required_keys:
            env_key = f"FIREBASE_{key.upper()}"
            if env_value := os.getenv(env_key):
                config[key] = env_value
            else:
                raise ValueError(f"Missing required Firebase config: {env_key}")
        return config

def get_service_account():
    """Get Firebase service account from file or environment variable"""
    try:
        # Try to load from file first
        with open('configs/firebase_service_account.json', 'r') as key_file:
            return json.load(key_file)
    except FileNotFoundError:
        # If file not found, try environment variable
        service_account_json = os.getenv('FIREBASE_SERVICE_ACCOUNT')
        if not service_account_json:
            raise ValueError("Missing FIREBASE_SERVICE_ACCOUNT environment variable")
        return json.loads(service_account_json)

# Get configurations
firebase_config_json = get_firebase_config()
service_account_key_json = get_service_account()

# Initialize the app with a service account
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_key_json)
    firebase_admin.initialize_app(cred)

# Initialize Firebase with configuration
firebase = pyrebase.initialize_app(firebase_config_json)
# Get database and auth instances
db = firebase.database()
authTodo = firebase.auth()


