import os
import sys
import uuid

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer

from firebase_admin import auth
from classes.schemas_dto import User
from database.firebase import db, authTodo

# Ajouter le répertoire parent au sys.path
sys.path.append(os.path.dirname(os.getcwd()))

# OAuth2 configuration
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')

def get_current_user(provided_token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = auth.verify_id_token(provided_token)
        decoded_token['idToken'] = provided_token
        return decoded_token
    except Exception:
        raise HTTPException(
            status_code=401,
            detail='Invalid or expired token'
        )

# Déclaration du routeur
router = APIRouter(
    prefix='/auth',
    tags=["Auth"]
)

# Inscription
@router.post('/signup', status_code=201)
async def signup(user_data: User):
    email = user_data.email
    password = user_data.password

    if len(password) < 6:
        raise HTTPException(
            status_code=400,
            detail="Password must be at least 6 characters long"
        )

    try:
        user = auth.create_user(email=email, password=password)

        user_data_dict = {
            "email": email,
            "uid": user.uid,
            "created_at": str(user.user_metadata.creation_timestamp)
        }

        try:
            db.child("users").child(user.uid).set(user_data_dict)
        except Exception as db_error:
            print(f"Warning: Could not write user data to database: {str(db_error)}")

        return JSONResponse(content={
            "message": f"User account created successfully for user {user.uid}",
            "user_id": user.uid
        })

    except auth.EmailAlreadyExistsError:
        raise HTTPException(
            status_code=409,
            detail=f"Account already exists for email {email}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while creating the account: {str(e)}"
        )

# Connexion
@router.post('/login')
async def create_swagger_token(user_credentials: OAuth2PasswordRequestForm = Depends()):
    try:
        user = authTodo.sign_in_with_email_and_password(
            email=user_credentials.username,
            password=user_credentials.password
        )
        return {
            'access_token': user['idToken'],
            'token_type': 'bearer'
        }
    except Exception:
        raise HTTPException(
            status_code=401,
            detail='Invalid credentials'
        )

# Endpoint sécurisé
@router.get('/me')
def secure_endpoint(user_data: dict = Depends(get_current_user)):
    return user_data
