from fastapi.testclient import TestClient
import pytest
from main import app
from unittest.mock import patch, MagicMock

# Mock 
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

client = TestClient(app)

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

def test_signup():
    """Test user signup"""
    with patch('firebase_admin.auth.create_user') as mock_create_user:
        mock_create_user.return_value.uid = "mocked_uid"
        response = client.post(
            "/auth/signup",
            json={"email": "test@example.com", "password": "password123"}
        )
        assert response.status_code == 200
        mock_create_user.assert_called_once()

def test_login_success():
    """Test successful login"""
    mock_response = {
        'idToken': 'test-token',
        'localId': 'test-user-id'
    }
    with patch('routers.router_auth.authTodo.sign_in_with_email_and_password', return_value=mock_response):
        response = client.post(
            "/auth/login",
            data={
                "username": "test@example.com",
                "password": "password123"
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        assert response.status_code == 200
        assert "access_token" in response.json()

def test_login_failure():
    """Test failed login"""
    with patch('routers.router_auth.authTodo.sign_in_with_email_and_password', side_effect=Exception("Invalid credentials")):
        response = client.post(
            "/auth/login",
            data={
                "username": "wrong@example.com",
                "password": "wrongpass"
            },
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        assert response.status_code == 401