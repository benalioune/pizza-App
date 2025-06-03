from fastapi import APIRouter, Depends, HTTPException
from classes.schemas_dto import Pizza, PizzaNoID, Order, OrderCreate
from typing import List, Dict
from routers.router_auth import get_current_user
from database.firebase import db
from datetime import datetime

import uuid



import uuid

router = APIRouter(
    prefix='/restaurant',
    tags=['Pizzeria Management']
)




@router.get("/menu", response_model=List[Pizza])
async def get_menu():
    """Récupère tout le menu des pizzas"""
    menu = db.child("menu").get().val()
    return [Pizza(**pizza) for pizza in menu.values()] if menu else []

@router.post("/menu", response_model=Pizza, status_code=201)
async def add_pizza(pizza_data: PizzaCreate, user_data: dict = Depends(get_current_user)):
    """Ajoute une nouvelle pizza (admin seulement)"""
    if user_data['role'] != 'admin':
        raise HTTPException(403, "Action réservée aux administrateurs")
    
    generated_id = str(uuid.uuid4())
    new_pizza = Pizza(id=generated_id, **pizza_data.dict())
    db.child("menu").child(generated_id).set(new_pizza.dict())
    return new_pizza

#---------------------------- ORDER MANAGEMENT ----------------------------#
@router.post("/orders", response_model=Order, status_code=201)
async def create_order(order_data: OrderCreate):
    """Crée une nouvelle commande"""
    order_id = str(uuid.uuid4())
    full_order = Order(
        id=order_id,
        status="reçue",
        order_time=datetime.now(),
        **order_data.dict()
    )
    
    # Gestion des stocks (exemple simplifié)
    for item in order_data.items:
        pizza = db.child("menu").child(item.pizza_id).get().val()
        for ingredient in pizza['ingredients']:
            db.child("inventory").child(ingredient).transaction(lambda curr: (curr or 0) - 1)
    
    db.child("orders").child(order_id).set(full_order.dict())
    return full_order

@router.patch("/orders/{order_id}/status", status_code=204)
async def update_order_status(order_id: str, new_status: str, user_data: dict = Depends(get_current_user)):
    """Met à jour le statut d'une commande"""
    valid_statuses = ["reçue", "en préparation", "prête", "livrée"]
    if new_status not in valid_statuses:
        raise HTTPException(400, "Statut invalide")
    
    db.child("orders").child(order_id).update({"status": new_status})

#---------------------------- TABLE MANAGEMENT ----------------------------#
@router.get("/tables", response_model=Dict[str, str])
async def get_table_status():
    """Récupère le statut de toutes les tables"""
    return db.child("tables").get().val() or {}

@router.post("/tables/{table_id}/occupy", status_code=201)
async def occupy_table(table_id: str):
    """Marque une table comme occupée"""
    db.child("tables").child(table_id).set({"status": "occupée", "order_id": None})
