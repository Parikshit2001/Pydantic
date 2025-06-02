from pydantic import BaseModel
from typing import Optional, List


class Lesson(BaseModel):
  lesson_id: int
  name: str
  description: str

class Module(BaseModel):
  module_id: int
  name: str
  description: str
  courses: Optional[List[Lesson]]

class Course(BaseModel):
  id: int
  name: str
  description: str
  modules: Optional[List[Module]]
