from fastapi import APIRouter, HTTPException
from utils.helpers import generateResponse
from models.todoModel import getAllTodos, createTodo
from models.todoModel import Todo

router = APIRouter(prefix="/api/todo", tags=["todo"])


@router.get("/", summary="Retrieve all todos")
async def fetchAllTodos():
    response = await getAllTodos()
    if response:
        return generateResponse("Successfully retrieved todos", response)

    raise HTTPException(404, "No todos available")


@router.post("/", summary="Create a new todo", response_model=Todo)
async def addTodo(todo: Todo):
    response = await createTodo(todo.model_dump())  # model_dump() return a dictionary
    if response:
        return generateResponse(
            "Todo created successfully",
            {"title": response.title, "description": response.description},
        )
    # return response

    raise HTTPException(400, "Failed to create todo")
