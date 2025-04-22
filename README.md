# Unix-Inspired Task Manager API

A FastAPI-based backend service that manages tasks in a Unix-inspired fashion, mimicking the concept of process management through HTTP endpoints.

## Features

- List all tasks (similar to `ls` command)
- Create new tasks (inspired by Unix `fork` system call)
- Task persistence using MongoDB
- RESTful API endpoints
- Comprehensive error handling
- Unit tests

## API Endpoints

### List All Tasks
- **GET** `/tasks`
  - Returns a list of all current tasks
  - Response includes task ID, name, status, and timestamps
  - **Test case:**
    ```bash
    curl -X GET "http://localhost:8000/tasks/"
    ```

### Create a Task
- **POST** `/tasks`
  - Creates a new task
  - Request body should include task details
  - Returns the created task with its ID
  - **Test case:**
    ```bash
    curl -X POST "http://localhost:8000/tasks/" \
        -H "Content-Type: application/json" \
        -d '{
              "name": "Test Task",
              "description": "This is a test task",
              "parent_id": "None"
            }'
    ```

### Get a Task
- **GET** `/tasks/{task_id}`
  - Replace `{task_id}` with the actual ID from the create response
  - Returns details of a specific task
  - **Test case:**
    ```bash
    curl -X GET "http://localhost:8000/tasks/{task_id}"
    ```

### Update a Task
- **PUT** `/tasks/{task_id}`
  - Replace `{task_id}` with the actual ID from the create response
  - Returns details of updated task
  - **Test case:**
    ```bash
    curl -X PUT "http://localhost:8000/tasks/{task_id}" \
        -H "Content-Type: application/json" \
        -d '{
              "name": "Updated Task",
              "status": "running"
            }'
    ```

### Delete Task
- **DELETE** `/tasks/{task_id}`
  - Removes a task from the system
  - **Test case:**
    ```bash
    curl -X DELETE "http://localhost:8000/tasks/{task_id}"
    ```

You can also use the Swagger UI for testing:
1. Start your FastAPI server:
```bash
uvicorn app.main:app --reload
```


## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
Create a `.env` file with:
```
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=taskmanager
```

4. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc 

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## **Contact Me**

For any inquiries or support, please reach out to:
- **Name**: Abhishek Singh
- **LinkedIn**: [My LinkedIn Profile](https://www.linkedin.com/in/abhishek-singh-bba2662a9)
- **Portfolio**: [Abhishek Singh](https://portfolio-abhishek-singh-nine.vercel.app/)
