from fastapi import APIRouter, Depends, HTTPException, Body
from typing import List, Dict
from datetime import datetime
import uuid

from classes.schemas_dto import Pizza, PizzaCreate, Order, OrderCreate
from routers.router_auth import get_current_user
from database.firebase import db

router = APIRouter(
    prefix='/restaurant',
    tags=['Pizzeria Management']
)

# --- MENU ---

@router.get("/menu", response_model=List[Pizza])
async def get_menu():
    """Récupère tout le menu des pizzas"""
    try:
        menu = db.child("menu").get().val()
        return [Pizza(**pizza) for pizza in menu.values()] if menu else []
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération du menu : {str(e)}")

@router.post("/menu", response_model=Pizza, status_code=201)
async def add_pizza(
    pizza_data: PizzaCreate,
    user_data: dict = Depends(get_current_user)
):
    """Ajoute une nouvelle pizza (admin uniquement)"""
    try:
        user_info = db.child("users").child(user_data['uid']).get().val()
        if not user_info or user_info.get('role') != 'admin':
            raise HTTPException(403, "Action réservée aux administrateurs")

        generated_id = str(uuid.uuid4())
        new_pizza = Pizza(id=generated_id, **pizza_data.dict())

        db.child("menu").child(generated_id).set(new_pizza.dict(), token=user_data['idToken'])
        return new_pizza
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'ajout de la pizza : {str(e)}")


# --- COMMANDES ---

@router.post("/orders", response_model=Order, status_code=201)
async def create_order(order_data: OrderCreate):
    """Crée une nouvelle commande"""
    try:
        order_id = str(uuid.uuid4())
        full_order = Order(
            id=order_id,
            status="reçue",
            order_time=datetime.now(),
            **order_data.dict()
        )

        # Vérification et mise à jour des stocks
        for item in order_data.items:
            pizza = db.child("menu").child(item.pizza_id).get().val()
            if not pizza:
                raise HTTPException(404, f"Pizza avec l'ID {item.pizza_id} introuvable.")

            for ingredient in pizza['ingredients']:
                current_stock = db.child("inventory").child(ingredient).get().val() or 0
                if current_stock < item.quantity:
                    raise HTTPException(400, f"Stock insuffisant pour l'ingrédient : {ingredient}")
                db.child("inventory").child(ingredient).set(current_stock - item.quantity)

        # Sauvegarde de la commande
        order_dict = full_order.dict()
        order_dict['order_time'] = order_dict['order_time'].isoformat()
        db.child("orders").child(order_id).set(order_dict)
        return full_order
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la création de la commande : {str(e)}")


@router.patch("/orders/{order_id}/status")
async def update_order_status(
    order_id: str,
    new_status: str = Body(..., embed=True),
    user_data: dict = Depends(get_current_user)
):
    """Met à jour le statut d'une commande (admin uniquement)"""
    try:
        user_info = db.child("users").child(user_data['uid']).get().val()
        if not user_info or user_info.get('role') != 'admin':
            raise HTTPException(403, "Action réservée aux administrateurs")

        valid_statuses = ["reçue", "en préparation", "prête", "livrée"]
        if new_status not in valid_statuses:
            raise HTTPException(400, "Statut invalide")

        db.child("orders").child(order_id).update({"status": new_status}, token=user_data['idToken'])
        return {"message": "Statut mis à jour avec succès"}
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la mise à jour du statut : {str(e)}")


# --- TABLES ---

@router.get("/tables", response_model=Dict[str, dict])
async def get_table_status():
    """Récupère le statut de toutes les tables"""
    try:
        return db.child("tables").get().val() or {}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de la récupération des tables : {str(e)}")

@router.post("/tables/{table_id}/occupy", status_code=201)
async def occupy_table(table_id: str):
    """Marque une table comme occupée"""
    try:
        db.child("tables").child(table_id).set({"status": "occupée", "order_id": None})
        return {"message": f"Table {table_id} marquée comme occupée."}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur lors de l'occupation de la table : {str(e)}")
