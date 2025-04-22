from fastapi.testclient import TestClient
from app.main import app
import pytest

client = TestClient(app)

def test_create_task():
    response = client.post(
        "/tasks/",
        json={
            "name": "Test Task",
            "description": "This is a test task",
            "parent_id": None
        }
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Test Task"
    assert data["description"] == "This is a test task"
    assert data["status"] == "created"
    return data["_id"]

def test_list_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0

def test_get_task():
    # First create a task
    task_id = test_create_task()
    
    # Then get it
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["_id"] == task_id

def test_update_task():
    # First create a task
    task_id = test_create_task()
    
    # Then update it
    response = client.put(
        f"/tasks/{task_id}",
        json={
            "name": "Updated Task",
            "status": "running"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["name"] == "Updated Task"
    assert data["status"] == "running"

def test_delete_task():
    # First create a task
    task_id = test_create_task()
    
    # Then delete it
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
    
    # Verify it's deleted
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404 

