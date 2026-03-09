from pydantic import BaseModel,EmailStr, Field
from typing import Optional
class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: EmailStr
    cgpa: float= Field(gt=0,lt=5, default=5, description="CGPA of the student")

new_student = {'name': "John",'age': 25, 'email': "john@example.com"}

#type coercing is also present in pydantic in which for example if we provide age as string it will convert it to int

student = Student(**new_student)

print(student)


#we can also provide default values

# class Student(BaseModel):
#     name: str="nistish"


# new_student = {}
