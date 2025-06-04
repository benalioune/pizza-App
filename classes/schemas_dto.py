from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime

# -------------------------
# To-Do Models
# -------------------------

class TodoNoID(BaseModel):
    name: str = Field(..., example="Acheter des tomates")


class Todo(TodoNoID):
    id: str = Field(..., example="todo_12345")


# -------------------------
# User Models
# -------------------------

class User(BaseModel):
    email: EmailStr = Field(..., example="benalioune6@gmail.com")
    password: str = Field(..., min_length=6, example="abcdef")


class UserLogin(User):
    class Config:
        schema_extra = {
            "example": {
                "email": "benalioune6@gmail.com",
                "password": "abcdef"
            }
        }


# -------------------------
# Pizza Models
# -------------------------

class PizzaBase(BaseModel):
    name: str = Field(..., example="Margherita")
    price: float = Field(..., gt=0, example=9.99)
    ingredients: List[str] = Field(..., example=["tomate", "mozzarella", "basilic"])
    size: str = Field(..., example="M", description="Taille de la pizza : S, M, L, XL")


class PizzaCreate(PizzaBase):
    pass


class Pizza(PizzaBase):
    id: str = Field(..., example="pizza_001")


# -------------------------
# Order Models
# -------------------------

class OrderItem(BaseModel):
    pizza_id: str = Field(..., example="pizza_001")
    quantity: int = Field(..., gt=0, example=2)
    customizations: Optional[List[str]] = Field(default_factory=list, example=["extra cheese", "sans olives"])


class OrderCreate(BaseModel):
    items: List[OrderItem]
    customer_name: str = Field(..., example="Jean Dupont")
    delivery_type: str = Field(..., example="sur place")  # ou "à emporter", "livraison"


class Order(OrderCreate):
    id: str = Field(..., example="order_123")
    status: str = Field(..., example="reçue")  # ou "en préparation", "prête", "livrée"
    order_time: datetime


# -------------------------
# Exemple de données fictives (à utiliser uniquement pour test local)
# -------------------------

users = [
    User(email="benalioune6@gmail.com", password="pass")
]

todos = [
    Todo(id="efe", name="Adama"),
    Todo(id="fef", name="Adrien"),
    Todo(id="dfd", name="Akbar"),
    Todo(id="frf", name="Alioune")
]
