import os
import pytest
from unittest.mock import patch

# Mock service account with all required fields
mock_service_account = {
    "type": "service_account",
    "project_id": "test-project",
    "private_key_id": "test-key-id",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCR7Yf9tjzxbSE8\nkZYGjxjP6yY6oo6UqhYBRjBc3Sw4qDL5Opk4+zX8IA+IQv2Nxe3JGRy1pJUyJrWI\nqGSKT4GlcHrVlV3wPxHJGjJMxGfcFZPB0cfJRGFRrKGhFDU+f9x07G32t6ZP3X3W\nPGGzHXBt2BgUgAWHe+87PvgBHXwDXjgxDrWJ1h4oHhGwOjkOTtqDtXpUzrUgNRfP\nOv6iLRsuHJjG6EBwFVXYwyqwN3jA4kEqGxGJvWvz0Tv+QXtcuoH7IXqP3+0QKYE9\nv5BPjK1BC1j1f7qMxCYhKPtNhJZCDwGhKWKGE1x2SC4TaVwk7FQsrR0J6tAqL7CC\nAgMBAAECggEABLKCJ7BwGVVpw5ftUdcKLprGt7zqbF4oNkjpvP3YlxV/NRFYCOqO\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-test@test-project.iam.gserviceaccount.com",
    "client_id": "123456789",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-test%40test-project.iam.gserviceaccount.com"
}

@pytest.fixture(autouse=True)
def setup_test_env():
    """Set up test environment variables and mocks"""
    # Set up environment variables
    os.environ['FIREBASE_APIKEY'] = 'test-api-key'
    os.environ['FIREBASE_AUTHDOMAIN'] = 'test.firebaseapp.com'
    os.environ['FIREBASE_DATABASEURL'] = 'https://test.firebaseio.com'
    os.environ['FIREBASE_PROJECTID'] = 'test-project'
    os.environ['FIREBASE_STORAGEBUCKET'] = 'test.appspot.com'
    os.environ['FIREBASE_MESSAGINGSENDERID'] = '123456789'
    os.environ['FIREBASE_APPID'] = '1:123456789:web:abcdef'
    os.environ['FIREBASE_SERVICE_ACCOUNT'] = str(mock_service_account)

    # Mock Firebase initialization
    with patch('database.firebase.get_service_account', return_value=mock_service_account):
        with patch('database.firebase.firebase_admin.initialize_app') as mock_init:
            with patch('database.firebase.pyrebase.initialize_app') as mock_pyrebase:
                mock_db = mock_pyrebase.return_value.database.return_value
                mock_auth = mock_pyrebase.return_value.auth.return_value
                yield {
                    'db': mock_db,
                    'auth': mock_auth
                } 