from models.todoModel import getAllTodos
from fastapi import APIRouter, HTTPException
from utils.helpers import generateResponse

router = APIRouter(prefix="/api/todo", tags=["todo"])


@router.get("/", summary="Retrieve all todos")
async def fetchAllTodos():
    response = await getAllTodos()
    if response:
        return generateResponse("Successfully retrieved todos", response)

    raise HTTPException(404, "No todos available")
