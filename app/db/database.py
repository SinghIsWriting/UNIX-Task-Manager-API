from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient
from pymongo.database import Database
from typing import Optional
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URL = os.getenv("MONGODB_URL", "mongodb://localhost:27017")
DATABASE_NAME = os.getenv("DATABASE_NAME", "taskmanager")

client: Optional[AsyncIOMotorClient] = None
database: Optional[Database] = None

async def connect_to_mongo():
    global client, database
    try:
        client = AsyncIOMotorClient(MONGODB_URL)
        database = client[DATABASE_NAME]
        # Test the connection
        await database.command("ping")
        print("Successfully connected to MongoDB!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise

async def close_mongo_connection():
    global client
    if client:
        client.close()
        client = None
        database = None

def get_database() -> Database:
    if database is None:
        raise RuntimeError("Database not initialized. Call connect_to_mongo() first.")
    return database 

