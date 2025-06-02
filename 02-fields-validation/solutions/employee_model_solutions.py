from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
  id: int
  name: str = Field(..., min_length=3, max_length=50, description="The name of the employee", examples=["Hitesh Choudhary"]) # ... means required
  department: Optional[str] = 'General'
  salary: float = Field(..., gt=10000)