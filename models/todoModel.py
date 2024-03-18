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


async def createTodo(todo):
    document = todo
    result = await collection.insert_one(document)

    # doc = await collection.find_one({"_id": result.inserted_id})

    return result
