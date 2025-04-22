from typing import List, Optional
from datetime import datetime, UTC
from bson import ObjectId
from app.models.task import Task
from app.db.database import get_database

class TaskRepository:
    @staticmethod
    async def get_tasks(skip: int = 0, limit: int = 100) -> List[Task]:
        tasks = []
        db = get_database()
        tasks_list = db.tasks.find().skip(skip).limit(limit)
        async for document in tasks_list:
            print(f"Found document: {document}")
            task = Task.from_mongo(document)
            print(f"Created task: {task}")
            if task:
                tasks.append(task)
        print(f"Returning {len(tasks)} tasks")
        return tasks

    @staticmethod
    async def get_task(task_id: str) -> Optional[Task]:
        if not ObjectId.is_valid(task_id):
            return None
        db = get_database()
        document = await db.tasks.find_one({"_id": ObjectId(task_id)})
        if document:
            return Task.from_mongo(document)
        return None

    @staticmethod
    async def create_task(task: Task) -> Task:
        task_dict = task.model_dump(exclude={'id'}, by_alias=True)
        task_dict["_id"] = ObjectId()
        task_dict["created_at"] = datetime.now(UTC)
        task_dict["updated_at"] = datetime.now(UTC)
        
        db = get_database()
        result = await db.tasks.insert_one(task_dict)
        created_task = await db.tasks.find_one({"_id": result.inserted_id})
        return Task.from_mongo(created_task)

    @staticmethod
    async def update_task(task_id: str, task_update: dict) -> Optional[Task]:
        if not ObjectId.is_valid(task_id):
            return None
            
        task_update["updated_at"] = datetime.now(UTC)
        db = get_database()
        result = await db.tasks.update_one(
            {"_id": ObjectId(task_id)},
            {"$set": task_update}
        )
        
        if result.modified_count:
            updated_task = await db.tasks.find_one({"_id": ObjectId(task_id)})
            return Task.from_mongo(updated_task)
        return None

    @staticmethod
    async def delete_task(task_id: str) -> bool:
        if not ObjectId.is_valid(task_id):
            return False
        db = get_database()
        result = await db.tasks.delete_one({"_id": ObjectId(task_id)})
        # print(f"Delete result: {result.deleted_count}", result)
        return result.deleted_count > 0
    
