# MongoDB driver
import motor.motor_asyncio

# Connect to MongoDB
client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://127.0.0.1:27017")

# Database
database = client.TodoList
