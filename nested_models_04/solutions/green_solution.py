from pydantic import BaseModel # type: ignore
from typing import List

# TODO: Create course model
# Each course has modules
# Each modules has lessons


class Lesson(BaseModel):
    lesson_id: int
    topic: str


class Module(BaseModel):
    module_id: int
    name: str
    lessons: List[Lesson]


class Course(BaseModel):
    course_id: int
    title: str
    modules: List[Module]
