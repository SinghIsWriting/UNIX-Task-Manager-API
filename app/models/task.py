from datetime import datetime, UTC
from typing import Optional, Any
from pydantic import BaseModel, Field, ConfigDict, field_validator
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v, handler):
        if v is None or v == "None":
            return None
        if not ObjectId.is_valid(v):
            raise ValueError("Invalid ObjectId")
        return ObjectId(v)

    @classmethod
    def __get_pydantic_json_schema__(cls, _schema_generator):
        return {"type": "string"}

class Task(BaseModel):
    model_config = ConfigDict(
        json_encoders={ObjectId: str},
        arbitrary_types_allowed=True,
        populate_by_name=True,
        json_schema_extra={
            "example": {
                "id": "507f1f77bcf86cd799439011",
                "name": "Sample Task",
                "description": "This is a sample task",
                "status": "created",
                "parent_id": None
            }
        }
    )
    
    id: Optional[str] = Field(default=None, alias="_id")
    name: str
    description: Optional[str] = None
    status: str = "created"  # created, running, completed, failed
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    parent_id: Optional[str] = None  # For fork-like behavior

    @field_validator('parent_id')
    @classmethod
    def validate_parent_id(cls, v):
        if v is None or v == "None":
            return None
        return v

    @classmethod
    def from_mongo(cls, data: dict):
        if not data:
            return None
        # Convert ObjectId to string before creating the instance
        data = data.copy()
        data['_id'] = str(data['_id'])
        if data.get('parent_id'):
            data['parent_id'] = str(data['parent_id'])
        return cls(**data)

    def model_dump(self, by_alias: bool = True, **kwargs):
        data = super().model_dump(by_alias=by_alias, **kwargs)
        if by_alias:
            if data.get('_id') is not None:
                data['_id'] = str(data['_id'])
        else:
            if data.get('id') is not None:
                data['id'] = str(data['id'])
        if data.get('parent_id') is not None:
            data['parent_id'] = str(data['parent_id'])
        return data 
    
