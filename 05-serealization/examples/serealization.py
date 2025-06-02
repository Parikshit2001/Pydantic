from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
  street: str
  city: str
  zip_code: str
  
class User(BaseModel):
  id: int
  name: str
  email: str
  is_Active: bool = True
  created_at: datetime
  address: Address
  tags: List[str] = []
  
  model_config = ConfigDict(
    json_encoders={
      datetime: lambda dt: dt.strftime("%Y-%m-%d %H:%M:%S"),
    }
  )
  
# create a user instance
user = User(
  id=1,
  name="John Doe",
  email="h5K4o@example.com",
  created_at=datetime(2024, 3, 13, 13, 15),
  address=Address(
    street="123 Main St",
    city="Anytown",
    zip_code="12345",
  ),
  tags=["user", "admin"]
)

# Using model_dump() -> dict
python_dict = user.model_dump()
print(python_dict)
print("================================================================================")
# Using model_dump_json() -> str
json_str = user.model_dump_json()
print(json_str)