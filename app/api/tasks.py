from fastapi import APIRouter, HTTPException, Depends
from typing import List
from app.models.task import Task
from app.schemas.task import TaskCreate, TaskUpdate, TaskInDB
from app.core.task_repository import TaskRepository

router = APIRouter()

@router.get("/", response_model=List[TaskInDB])
async def list_tasks(skip: int = 0, limit: int = 100):
    """
    List all tasks (similar to Unix 'ls' command)
    """
    tasks = await TaskRepository.get_tasks(skip=skip, limit=limit)
    return tasks

@router.post("/", response_model=TaskInDB, status_code=201)
async def create_task(task: TaskCreate):
    """
    Create a new task (similar to Unix 'fork' system call)
    """
    new_task = Task(
        name=task.name,
        description=task.description,
        parent_id=task.parent_id
    )
    created_task = await TaskRepository.create_task(new_task)
    return created_task

@router.get("/{task_id}", response_model=TaskInDB)
async def get_task(task_id: str):
    """
    Get a specific task by ID
    """
    task = await TaskRepository.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.put("/{task_id}", response_model=TaskInDB)
async def update_task(task_id: str, task_update: TaskUpdate):
    """
    Update a task's details
    """
    task = await TaskRepository.get_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    update_data = task_update.dict(exclude_unset=True)
    updated_task = await TaskRepository.update_task(task_id, update_data)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/{task_id}", status_code=200)
async def delete_task(task_id: str):
    """
    Delete a task
    """
    success = await TaskRepository.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully", "status": 200}

