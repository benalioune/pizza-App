from fastapi.testclient import TestClient
import os
import sys
import pytest
from unittest.mock import patch, MagicMock

sys.path.append(os.getcwd())
sys.path.append('./app')

# Mock Firebase configuration
os.environ['FIREBASE_APIKEY'] = 'test-api-key'
os.environ['FIREBASE_AUTHDOMAIN'] = 'test.firebaseapp.com'
os.environ['FIREBASE_DATABASEURL'] = 'https://test.firebaseio.com'
os.environ['FIREBASE_PROJECTID'] = 'test-project'
os.environ['FIREBASE_STORAGEBUCKET'] = 'test.appspot.com'
os.environ['FIREBASE_MESSAGINGSENDERID'] = '123456789'
os.environ['FIREBASE_APPID'] = '1:123456789:web:abcdef'

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
def mock_firebase():
    """Mock Firebase initialization and database operations"""
    with patch('database.firebase.get_service_account', return_value=mock_service_account):
        with patch('database.firebase.firebase_admin.initialize_app') as mock_init:
            with patch('database.firebase.pyrebase.initialize_app') as mock_pyrebase:
                mock_db = MagicMock()
                mock_auth = MagicMock()
                mock_pyrebase.return_value.database.return_value = mock_db
                mock_pyrebase.return_value.auth.return_value = mock_auth
                yield {
                    'db': mock_db,
                    'auth': mock_auth
                }

from main import app

client = TestClient(app)

def test_docs():
    res = client.get("/docs")
    assert res.status_code == 200


# Ecrire test /redocs
    
def test_redoc():
    res = client.get("/redoc")
    assert res.status_code == 200

def test_get_menu():
    """Test getting the menu endpoint"""
    mock_menu = [
        {
            "id": "1",
            "name": "Margherita",
            "price": 10.99,
            "ingredients": ["tomato sauce", "mozzarella", "basil"],
            "size": "M"
        }
    ]
    with patch('routers.router_restau.db') as mock_db:
        mock_db.child().get().val.return_value = {"1": mock_menu[0]}
        response = client.get("/restaurant/menu")
        assert response.status_code == 200
        assert response.json() == mock_menu