# Unix-Inspired Task Manager API

A FastAPI-based backend service that manages tasks in a Unix-inspired fashion, mimicking the concept of process management through HTTP endpoints.

### Deployed APIs Docs: https://unixtask.devhome.me/docs

## Features

- List all tasks (similar to `ls` command)
- Create new tasks (inspired by Unix `fork` system call)
- Task persistence using MongoDB
- RESTful API endpoints
- Comprehensive error handling
- Unit tests

## Demo
https://github.com/user-attachments/assets/d4044530-cbc0-45ae-9dd9-d22455b373e5

## API Endpoints

### List All Tasks
- **GET** `/tasks`
  - Returns a list of all current tasks
  - Response includes task ID, name, status, and timestamps
  - **Test case (Deployed API):**
    ```bash
    curl -X GET "https://unixtask.devhome.me/tasks/"
    ```
  - **Test case (Local API):**
    ```bash
    curl -X GET "http://localhost:8000/tasks/"
    ```

### Create a Task
- **POST** `/tasks`
  - Creates a new task
  - Request body should include task details
  - Returns the created task with its ID
  - **Test case (Deployed API):**
    ```bash
    curl -X POST "https://unixtask.devhome.me/tasks/" \
        -H "Content-Type: application/json" \
        -d '{
              "name": "Test Task",
              "description": "This is a test task",
              "parent_id": "None"
            }'
    ```
  - **Test case (Local API):**
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
  - **Test case (Deployed API):**
    ```bash
    curl -X GET "https://unixtask.devhome.me/tasks/{task_id}"
    ```
  - **Test case (Local API):**
    ```bash
    curl -X GET "http://localhost:8000/tasks/{task_id}"
    ```

### Update a Task
- **PUT** `/tasks/{task_id}`
  - Replace `{task_id}` with the actual ID from the create response
  - Returns details of updated task
  - **Test case (Deployed API):**
    ```bash
    curl -X PUT "https://unixtask.devhome.me/tasks/{task_id}" \
        -H "Content-Type: application/json" \
        -d '{
              "name": "Updated Task",
              "status": "running"
            }'
    ```
  - **Test case (Local API):**
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
  - **Test case (Deployed API):**
    ```bash
    curl -X DELETE "https://unixtask.devhome.me/tasks/{task_id}"
    ```
  - **Test case (Local API):**
    ```bash
    curl -X DELETE "http://localhost:8000/tasks/{task_id}"
    ```

You can also use the Swagger UI for testing:
1. Start your FastAPI server:
```bash
uvicorn app.main:app --reload
```


## Setup

1. Clone repository
```bash
git clone https://github.com/SinghIsWriting/UNIX-Task-Manager-API.git
cd UNIX-Task-Manager-API
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with:
```
MONGODB_URL=mongodb://localhost:27017
DATABASE_NAME=taskmanager
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

## API Documentation

Once the server is running, visit:
### Deployed API Docs
- Swagger UI: https://unixtask.devhome.me/docs
- ReDoc: https://unixtask.devhome.me/redoc 
### Local API Docs
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
