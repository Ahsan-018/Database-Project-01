from models.database import Base, engine, SessionLocal
from models.department import Department
from models.employee import Employee

Base.metadata.create_all(engine)
print("Tables created successfully!")

session = SessionLocal()

# Insert Departments
dept1 = Department(department_name="IT")
session.add(dept1)

dept2 = Department(department_name="HR")
session.add(dept2)

session.commit()

print("Departments added successfully!")

#Inserting in Employees
emp1 = Employee(name="Ahsan Mahmood", email="ahsan_mahmood@gmail.com", department_id=dept1.department_id)
emp2 = Employee(name="Talha Rauf", email="talha_rauf@gmail.com", department_id=dept2.department_id)
emp3 = Employee(name="Saad Ali", email="saad_ali@gmail.com", department_id=dept1.department_id)

session.add_all([emp1, emp2, emp3])
session.commit()

print("Employees added successfully!")

# Retrieving the Data
print("\nEmployees List:")

employees = session.query(Employee).all()

for emp in employees:
    department = session.query(Department).filter_by(department_id=emp.department_id).first()
    print(f"ID: {emp.employee_id}, Name: {emp.name}, Email: {emp.email}, Department: {department.department_name}")

# Updating department
employee_to_update = session.query(Employee).filter_by(name="Talha Rauf").first()

if employee_to_update:
    employee_to_update.department_id = dept1.department_id
    session.commit()
    print("Employee department updated successfully!")

# Deleting Department
department_to_delete = session.query(Department).filter_by(department_name="HR").first()

if department_to_delete:
    employees_in_dept = session.query(Employee).filter_by(department_id=department_to_delete.department_id).all()
    
    if not employees_in_dept:
        session.delete(department_to_delete)
        session.commit()
        print("Department deleted successfully!")
    else:
        print("Cannot delete department. Employees exist.")
    
# updated salary
employee_salary_update = session.query(Employee).filter_by(name="Ahsan Mahmood").first()

if employee_salary_update:
    employee_salary_update.salary = 80000
    session.commit()
    print("Salary updated successfully!")




