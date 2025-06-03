
from fastapi import APIRouter, Depends, HTTPException
from classes.schemas_dto import Todos
from classes.schemas_dto import Todo
from classes.schemas_dto  import TodoNoID
from typing import List
from routers.router_auth import get_current_user

from database.firebase import db



import uuid



router = APIRouter(
    prefix='/todos',
    tags=['Todos']
)


# Verbs + Endpoints
@router.get("/todos", response_model=List[Todo])
async def get_todo(user_data: int= Depends(get_current_user)):
    queryResults = db.child("todo").get(user_data['idToken']).val()
    if not queryResults : return []
    todoArray = [Todo(**value) for value in queryResults.values()]
    return todoArray 




@router.post('/todos', response_model=Todo, status_code=201)
async def create_todo(givenName:str):
    # génération de l'identifiant unique
    generatedId=uuid.uuid4()
    # création de l'object/dict Todo 
    newTodo= Todo(id=str(generatedId), name=givenName)
    # Ajout du nouveau Todo dans la List/Array
    Todos.append(newTodo)
    
    db.child("todo").child(generatedId).set(newTodo.model_dump())
    # Réponse définit par le Todo avec son ID
    return newTodo



@router.get('/todos/{todo_id}', response_model=Todo)
async def get_todo_by_id(todo_id: str, user_data: int= Depends(get_current_user)):
    queryResult = db.child('todo').child(todo_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Todo not found") 
    return queryResult




@router.patch('/{todo_id}', status_code=204)
async def todo_update(todo_id: str, todo: TodoNoID, user_data: int= Depends(get_current_user)):
    queryResult = db.child('todo').child(todo_id).get(user_data['idToken']).val()
    if not queryResult : raise HTTPException(status_code=404, detail="Todo not found") 
    updatedTodo = Todo(id=todo_id, **todo.model_dump())
    return db.child('todo').child(todo_id).update(data=updatedTodo.model_dump(), token=user_data['idToken'])

@router.delete("/{t_id}", status_code=202, response_model=str)
async def todo_delete(todo_id: str, user_data: int= Depends(get_current_user)) :
    queryResult = db.child('todo').child(todo_id).get(user_data['idToken']).val()
    if not queryResult : 
        raise HTTPException(status_code=404, detail="Todo not found")
    db.child('todo').child(todo_id).remove(token=user_data['idToken'])
    return "Todo deleted"

