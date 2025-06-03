
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime



# DTO : Data Transfert Object ou Schema
# Représente la structure de la données (data type) en entrée ou en sortie de notre API.
# Model Pydantic = Datatype

class TodoNoID(BaseModel):
    name: str
    

class Todo(BaseModel):
    id: str
    name: str
    
    
class User(BaseModel):

    email: str
    password: str
    

class UserLogin(BaseModel):

    email: str
    password: str
    
# define how we except the request body to be
class Config:
    schema_extra={
        "exemple": {
            "email": "benalioune6@gmail.com",
            "password": "abcdef"
        }
    }
    

    
    
users = [
    
    User(email="benalioune6@gmail.com", password="pass")
    
]
    

Todos = [
    Todo(id="efe", name="Adama"),
    Todo(id="fef", name="Adrien"),
    Todo(id="dfd", name="Akbar"),
    Todo(id="frf", name="Alioune")
]



class PizzaBase(BaseModel):
    name: str
    price: float
    ingredients: List[str]
    size: str  # S/M/L/XL

class PizzaCreate(PizzaBase):
    pass

class Pizza(PizzaBase):
    id: str

class OrderItem(BaseModel):
    pizza_id: str
    quantity: int
    customizations: Optional[List[str]] = None

class OrderCreate(BaseModel):
    items: List[OrderItem]
    customer_name: str
    delivery_type: str  # sur place/à emporter/livraison

class Order(OrderCreate):
    id: str
    status: str  # reçue/en préparation/prête/livrée
    order_time: datetime
