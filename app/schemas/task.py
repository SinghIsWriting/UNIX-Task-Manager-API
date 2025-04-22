from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId

class TaskBase(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        json_encoders={ObjectId: str}
    )
    
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None

class TaskCreate(TaskBase):
    name: str
    description: Optional[str] = None
    parent_id: Optional[str] = None

class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None

class TaskInDB(TaskBase):
    model_config = ConfigDict(
        from_attributes=True,
        populate_by_name=True,
        json_encoders={ObjectId: str}
    )
    
    id: str = Field(alias="_id")
    status: str
    created_at: datetime
    updated_at: datetime
    parent_id: Optional[str] = None 

