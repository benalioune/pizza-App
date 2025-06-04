# import du framework
from fastapi import FastAPI , HTTPException


#Import des routers

import routers.router_auth

import routers.router_todos

import routers.router_restau


# Documentation
from documentation.description import api_description
# from documentation.tags import tags_metadata


#initialisation de l'API
app  = FastAPI(
    title = "Restaurant Management API",
    description=api_description,
    # openapi_tags=tags_metadata # tagsmetadata definit au dessus
)



# Ajouter les routers dédiés
app.include_router(routers.router_auth.router)
app.include_router(routers.router_todos.router)
app.include_router(routers.router_restau.router)
