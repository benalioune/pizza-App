



# import du framework
from fastapi import FastAPI , HTTPException

from fastapi.middleware.cors import CORSMiddleware
#Import des routers

# import routers.router_auth

# import routers.router_todos

# import routers.router_restau
import routers.router_pizzeria


# Documentation
from documentation.description import api_description
# from documentation.tags import tags_metadata


#initialisation de l'API
app  = FastAPI(
    title = "Todo List",
    description=api_description,
    # openapi_tags=tags_metadata # tagsmetadata definit au dessus
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # ou ["*"] pour tout autoriser
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ajouter les routers dédiés
# app.include_router(routers.router_auth.router)
# app.include_router(routers.router_todos.router)
# app.include_router(routers.router_restau.router)
app.include_router(routers.router_pizzeria.router)
