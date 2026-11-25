from sqlalchemy import Column, Integer, String, ForeignKey
from models.database import Base

class Employee(Base):
    __tablename__ = "employees"

    employee_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    salary = Column(Integer)
    department_id = Column(Integer, ForeignKey("departments.department_id"))
