from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
  street: str
  city: str
  postal_code: str
  
class User(BaseModel):
  id: int
  name: str
  address: Address
  
class Comment(BaseModel):
  id: int
  content: str
  replies: Optional[List['Comment']] = None # Self replication or self referencing or forward referencing
  user: User
  
Comment.model_rebuild() # When doing self referencing

address = Address(street="123 Main St", city="Anytown", postal_code="12345")
user = User(id=1, name="John Doe", address=address)
comment = Comment(id=1, content="This is a comment", replies=[
  Comment(id=2, content="This is a reply to the comment", user=user),
  Comment(id=3, content="This is another reply to the comment", user=user)
  ], user=user)