from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.tasks import router as tasks_router
from app.db.database import connect_to_mongo, close_mongo_connection

app = FastAPI(
    title="Unix-Inspired Task Manager API",
    description="A FastAPI-based backend service that manages tasks in a Unix-inspired style",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])

@app.on_event("startup")
async def startup_db_client():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_db_client():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {
        "message": "Welcome to the Unix-Inspired Task Manager API",
        "docs_url": "/docs",
        "redoc_url": "/redoc"
    } 


