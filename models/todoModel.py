from pydantic import BaseModel
from config.dbConfig import database


class Todo(BaseModel):
    title: str
    description: str


collection = database.todo


async def getAllTodos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos
