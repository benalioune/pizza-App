
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime




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
    delivery_type: str  

class Order(OrderCreate):
    id: str
    status: str  
    order_time: datetime
