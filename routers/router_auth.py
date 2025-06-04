# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.responses import JSONResponse
# from fastapi.security.oauth2 import OAuth2PasswordRequestForm
# import os
# import sys


# # Add the parent directory to the Python path
# sys.path.append(os.path.dirname(os.getcwd()))

# from database.firebase import db


# from fastapi.security import OAuth2PasswordBearer

# from classes.schemas_dto import User
# from firebase_admin import auth
# from database.firebase import authTodo


# import uuid

# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/login')
# def get_current_user(provided_token: str = Depends(oauth2_scheme)):
#     decoded_token = auth.verify_id_token(provided_token)
#     decoded_token['idToken'] = provided_token
#     return decoded_token

# router  =  APIRouter(
    
#     tags=["Auth"],
#     prefix='/auth'
    
# )
# #signup endPoint
# @router.post('/signup', status_code=201)
# async def signup(user_data:User):
#     email = user_data.email
#     password = user_data.password
    
#     # Validate password length
#     if len(password) < 6:
#         raise HTTPException(
#             status_code=400,
#             detail="Password must be at least 6 characters long"
#         )
    
#     try:
#         # Create user in Firebase Authentication
#         user = auth.create_user(
#             email=email,
#             password=password
#         )
        
#         try:
#             # Try to store additional user data in Realtime Database
#             user_data_dict = {
#                 "email": email,
#                 "uid": user.uid,
#                 "created_at": str(user.user_metadata.creation_timestamp)
#             }
#             db.child("users").child(user.uid).set(user_data_dict)
#         except Exception as db_error:
#             # If database write fails, still return success since user was created
#             print(f"Warning: Could not write user data to database: {str(db_error)}")
            
#         return JSONResponse(content={
#             "message": f"User account created successfully for user {user.uid}",
#             "user_id": user.uid
#         })
        
#     except auth.EmailAlreadyExistsError:
#         raise HTTPException(
#             status_code=409,  # Conflict
#             detail=f"Account already exists for email {email}"
#         )
#     except Exception as e:
#         raise HTTPException(
#             status_code=500,
#             detail=f"An error occurred while creating the account: {str(e)}"
#         )
    

   

# #login endPoint

# @router.post('/login')
# async def create_swagger_token(user_credentials: OAuth2PasswordRequestForm = Depends()):
#     try:
#         user = authTodo.sign_in_with_email_and_password(
#             email=user_credentials.username, 
#             password=user_credentials.password
#         )
#         token = user['idToken']
#         return {
#             'access_token': token,
#             'token_type': 'bearer'
#         }
#     except Exception as e:
#         raise HTTPException(
#             status_code=401,
#             detail='Invalid credentials'
#         )

               

 
# #protect route to get personal data 
# @router.get('/me')
# def secure_endpoint(user_data: dict = Depends(get_current_user)):
#     return user_data
