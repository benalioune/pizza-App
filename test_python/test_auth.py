from fastapi.testclient import TestClient
from main import app  # Assurez-vous d'ajuster le chemin si nécessaire
from unittest.mock import patch, MagicMock
import pytest

# Mock de la fonction auth.create_user pour éviter d'appeler Firebase lors des tests
@patch("firebase_admin.auth.create_user")
def test_signup(mock_create_user):
    client = TestClient(app)

    # Données utilisateur fictives pour le test
    user_data = {"email": "test@example.com", "password": "password"}

    # Simuler la création d'utilisateur dans Firebase
    mock_create_user.return_value.uid = "mocked_uid"

    # Exécuter la requête de test
    response = client.post("/auth/signup", json=user_data)

    assert response.status_code == 200

    # Assurez-vous que la fonction create_user a été appelée avec les bonnes données
    mock_create_user.assert_called_once_with(email=user_data["email"], password=user_data["password"])

    print(f"User data: {user_data}")
    print(f"Mock create_user arguments: {mock_create_user.call_args}")

client = TestClient(app)

@pytest.fixture(autouse=True)
def mock_firebase():
    """Mock Firebase initialization and database operations"""
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

def test_login_success():
    """Test successful login"""
    mock_response = {
        'idToken': 'test-token',
        'localId': 'test-user-id'
    }
    with patch('routers.router_auth.authTodo.sign_in_with_email_and_password', return_value=mock_response):
        response = client.post(
            "/auth/login",
            json={"email": "test@example.com", "password": "password123"}
        )
        assert response.status_code == 200
        assert "access_token" in response.json()

def test_login_failure():
    """Test failed login"""
    with patch('routers.router_auth.authTodo.sign_in_with_email_and_password', side_effect=Exception("Invalid credentials")):
        response = client.post(
            "/auth/login",
            json={"email": "wrong@example.com", "password": "wrongpass"}
        )
        assert response.status_code == 401