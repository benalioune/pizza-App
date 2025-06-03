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
os.environ['FIREBASE_SERVICE_ACCOUNT'] = '{"type": "service_account", "project_id": "test"}'

from main import app

client = TestClient(app)

def test_docs():
    res = client.get("/docs")
    assert res.status_code == 200


# Ecrire test /redocs
    
def test_redoc():
    res = client.get("/redoc")
    assert res.status_code == 200

@pytest.fixture
def mock_firebase():
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