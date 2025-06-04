from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
import uuid

router = APIRouter(
    prefix='/api',
    tags=['Basic Mock API']
)

# ─── Data Storage (in-memory) ───────────────────────────────────────────────

pizzas = []
users = []
orders = []

# ─── Pydantic Models ────────────────────────────────────────────────────────

class Pizza(BaseModel):
    id: str
    name: str
    price: float

class PizzaCreate(BaseModel):
    name: str
    price: float

class User(BaseModel):
    id: str
    name: str
    email: str

class UserCreate(BaseModel):
    name: str
    email: str

class OrderItem(BaseModel):
    id: str
    name: str
    price: float
    qty: int

class Order(BaseModel):
    items: List[OrderItem]
    total: float



# ─── Pizzas ─────────────────────────────────────────────────────────────────

@router.get("/pizzas", response_model=List[Pizza])
def get_pizzas():
    return pizzas

@router.post("/pizzas", response_model=Pizza, status_code=201)
def create_pizza(pizza: PizzaCreate):
    new_pizza = Pizza(id=str(uuid.uuid4()), **pizza.dict())
    pizzas.append(new_pizza)
    return new_pizza

@router.put("/pizzas/{pizza_id}", response_model=Pizza)
def update_pizza(pizza_id: str, updated_data: PizzaCreate):
    for p in pizzas:
        if p.id == pizza_id:
            p.name = updated_data.name
            p.price = updated_data.price
            return p
    raise HTTPException(status_code=404, detail="Pizza not found")

@router.delete("/pizzas/{pizza_id}", status_code=204)
def delete_pizza(pizza_id: str):
    global pizzas
    pizzas = [p for p in pizzas if p.id != pizza_id]

# ─── Users ──────────────────────────────────────────────────────────────────

@router.get("/users", response_model=List[User])
def get_users():
    return users

@router.post("/users", response_model=User, status_code=201)
def create_user(user: UserCreate):
    new_user = User(id=str(uuid.uuid4()), **user.dict())
    users.append(new_user)
    return new_user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: str, updated_data: UserCreate):
    for u in users:
        if u.id == user_id:
            u.name = updated_data.name
            u.email = updated_data.email
            return u
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{user_id}", status_code=204)
def delete_user(user_id: str):
    global users
    users = [u for u in users if u.id != user_id]

# ─── Orders ─────────────────────────────────────────────────────────────────

@router.get("/orders", response_model=List[Order])
def get_orders():
    return orders

@router.post("/orders", response_model=Order, status_code=201)
async def create_order(order_data: Order):
    try:
        order_id = str(uuid.uuid4())
        full_order = Order(
            id=order_id,
            status="reçue",
            items=order_data.items,
            total=order_data.total
        )

        order_dict = full_order.dict()
        orders.append(order_dict)
        return full_order
    except HTTPException as he:
        raise he
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error creating order: {str(e)}")
