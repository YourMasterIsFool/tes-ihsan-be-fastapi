from pydantic import BaseModel, field_validator

class CreateTaskDto(BaseModel):
    name: str
    
    
class UpdateTaskDto(BaseModel):
    name: str
    

