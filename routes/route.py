from fastapi import APIRouter
from models.todos import Todo
from config.database import collection_name
from schema.schemas import list_serial
from bson import ObjectId
from typing import List


router = APIRouter()


# GET Request Method
@router.get("/", response_model=List)
async def get_todos():
    todos = list_serial(collection_name.find())
    return todos


# POST Request Method
@router.post("/", response_model=str)
async def post_todo(todo: Todo):
    collection_name.insert_one(dict(todo))
    return "New Todo has been created"


# PUT Request Method
@router.put("/{id}", response_model=str)
async def put_todo(id: str, todo: Todo):
    collection_name.find_one_and_update({"_id": ObjectId(id)}, {"$set": dict(todo)})
    return "Todo has been updated"


# DELETE Request Method
@router.delete("/{id}", response_model=str)
async def delete_todo(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return "Todo has been deleted"
