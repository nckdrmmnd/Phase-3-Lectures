import sqlite3
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine
from sqlalchemy.orm import Session, sessionmaker, relationship, declarative_base, validates #imports a database session
from sqlalchemy.exc import IntegrityError # importing errors
Base = declarative_base() 



class Warehouse(Base):
  
  __tablename__ = "Warehouses"
  id = Column(Integer, primary_key=True)
  location = Column(String, nullable=False)
  sqft = Column(Integer, nullable=False)
  revenue = Column(Integer, nullable=False)
  #region_id = Column(Integer, nullable=False)
  
  employees = relationship("Employee",secondary="Region", back_populates="warehouse")
  
  
class Employee(Base):
  
  __tablename__ = "Employees"
  id = Column(Integer, primary_key=True)
  name = Column(String, nullable=False)
  salary = Column(Integer, nullable=False)
  length_of_employment = Column(Integer, nullable=False)
  
  warehouse = relationship("Warehouse",secondary="Region", back_populates="employees")
  warehouse_id = Column(Integer, ForeignKey("Warehouses.id"))
  
  
class Region(Base):
  
  __tablename__ = "Region"
  id = Column(Integer, primary_key=True)
  employee_id = Column(Integer, ForeignKey("Employees.id"))
  warehouse_id = Column(Integer, ForeignKey("Warehouses.id"))
  total_employees = Column(Integer,nullable=False)
  
  
if __name__ =="__main__":
  
  engine = create_engine("sqlite:///biztracker.db")
  # Employee.__table__.drop(engine)
  # Warehouse.__table__.drop(engine)
  # Region.__table__.drop(engine)
  
  Base.metadata.create_all(engine)
  Session = sessionmaker(bind=engine)
  session = Session()
  
  while True:
    print("-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-")
    print("| Welcome to Logistics Management Tool of Operational Oversight of Regional Revenue Development or (LMTOORRD for short)")
    print("|  1: Add an Employee or Warehouse")
    print("|  2: Delete a Employee or Warehouse")
    print("|  3: Update a Employee or Warehouse")
    print("|  4: View total gross for a Warehouse by ID")
    print("|  5: Find a Employee or Warehouse by name/location")
    print("|  6: tbd")
    print("|  7: ???")
    print("|  8: Exit")
    print("-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-+-=-=-")
    usr_input = input("Enter a number (1-8) and press enter to continue: ")
    
    if usr_input == "1":
      while True:
        seconday_input = input("Would you like to add an 1 - employee, 2 - warehouse, 8 - exit: ")
        if seconday_input == "1":
          print("Entering a new Employee to the database.")#Start with name, salary, length of employment, warehouse id"
          name = input("Enter a Name: ")
          salary = int(input("Enter salary amount, no commas: "))
          length = int(input("How long have they worked here in months, 0 by default: "))
          warehouse = int(input("What warehouse ID: "))
          new_employee = Employee(name=name, salary=salary, length_of_employment=length, warehouse_id= warehouse)
          print(f"Successfully added a new employee: {new_employee.name}, ${new_employee.salary}, {new_employee.length_of_employment}, at warehouse {new_employee.warehouse_id}")
          session.add(new_employee)
          session.commit()
          break
          
        elif seconday_input == "2":
          print("Entering a new Warehouse")
          location = input("Enter location:  ")
          sqft = int(input("Enter total sqft, no commas: "))
          revenue = int(input("Enter how much revenue it makes, no commas: "))
          new_warehouse = Warehouse(location=location, revenue=revenue, sqft=sqft)
          print(f"Successfully added new warehouse: {new_warehouse.location}, {new_warehouse.sqft}, making ${new_warehouse.revenue}")
          session.add(new_warehouse)
          session.commit()
          break
        elif seconday_input == "8":
          break
        else:
          print("Please enter a number: 1, 2 or 8")
        
    elif usr_input == "2":
      while True:
        sec_npt = input("Permanetly delete an 1 - Employee or a 2 - Warehouse, 8 - exit: ")
        if sec_npt == "1":
          del_emp_id = int(input("Enter Employee ID: "))
          delt_emp = session.query(Employee).filter_by(id=del_emp_id).first()
          print(f"Successfully deleted Employee {delt_emp.name}, id: {delt_emp.id}")
          session.delete(delt_emp)
          session.commit()
          break
          
        elif sec_npt == "2":
          del_ware_id = int(input("Enter the Warehouse ID: "))
          delt_ware = session.query(Warehouse).filter_by(id=del_ware_id).first()
          print(f"Successfully deleted Warehouse at {delt_ware.location}, id {delt_ware.id}")
          session.delete(delt_ware)
          session.commit()
          break
        
        elif sec_npt == "8":
          break
        else:
          print("Please enter a number: 1, 2 or 8")
        
    elif usr_input == "3":
      while True:
        seconday_input = input("Update an 1 - Employee or a 2 - Warehouse, 8 - exit: ")
        if seconday_input == "1":
          update_id = int(input("Enter the ID of the Employee: "))
          updated_emp = session.query(Employee).filter_by(id=update_id).first()
          if updated_emp:
            name = input("Enter a new name or press enter to keep current name: ")
            salary = input("Enter a new salary, no commas, or press enter to keep current salary: ")
            length_of_emp = input("Enter in new amount of months, no commas, or press enter to keep current months: ")
            if name:
              updated_emp.name = name
            if salary:
              try:
                updated_emp.salary = int(salary)
              except ValueError:
                print("Please enter a valid number of money, no commas or dollar signs")
                continue
            if length_of_emp:
              try:  
                updated_emp.length_of_employment = int(length_of_emp)
              except ValueError:
                print("Please enter a valid number of months, no commas")
                continue
            print(f"Successfully updated Employee {updated_emp.name}, salary: ${updated_emp.salary}, length of employment: {updated_emp.length_of_employment}")
            session.commit()
            break
                
            
        elif seconday_input =="2":
          update_id = int(input("Enter the ID of the Warehouse: "))
          updated_ware = session.query(Warehouse).filter_by(id=update_id).first()
          if updated_ware:
            location = input("Enter a new location or press enter to keep current location:")
            sqft = input("Enter a new total squarefeet, no commas, or press enter to keep current squarefeet: ")
            revenue = input("Enter in new amount of revenue, no commas, or press enter to keep current revenue: ")
            if location:
              updated_ware.location = location
            if sqft:
              try:
                updated_ware.sqft = int(sqft)
              except ValueError:
                print("Please enter a valid number of sqft, only the numbers no sign")
                continue
            if revenue:
              try:  
                updated_emp.revenue = int(revenue)
              except ValueError:
                print("Please enter a valid number of money, no commas or dollar signs")
                continue
            print(f"Successfully updated Warehouse {updated_ware.location}, squarefeet: {updated_ware.sqft}sqft, revenue: ${updated_ware.revenue}")
            session.commit()
            break
        elif seconday_input == "8":
          break
        else:
          print("Please enter a number: 1, 2 or 8")
          
          
    elif usr_input == "4":
      while True:
        query_id = input("Enter the ID of the warehouse (88 to exit): ")
        if query_id == "88":
          break
        try:
          query_id = int(query_id)
        except ValueError:
          print("ID must be a number")
          continue
        if query_id:#core logic for the method
          total_employees = session.query(Employee).filter_by(warehouse_id=query_id).all()
          warehouse = session.query(Warehouse).filter_by(id=query_id).first()
          i=0
          salary_amt=0
          for employee in total_employees:
            # print(f"{employee.name} has a salary of ${employee.salary}")
            salary_amt = salary_amt + employee.salary
            i += 1
          gross_percent = round((salary_amt / warehouse.revenue), 3)
          print(f"Warehouse {query_id}, is making ${warehouse.revenue} and spending {gross_percent}% on employees. Total number of Employees: {i} employees that total ${salary_amt} spent. ")
      
    elif usr_input == "5":#find a employee by name,
      while True:
        seconday_input = input("Enter 1 for employee, 2 for warehouse, or 8 to exit: ")
        if seconday_input == "1":
          while True:
            query_emp_name = input("Enter the name of employee (Case Sensitive) 8 to exit: ")
            query_emp_retrieved = session.query(Employee).filter_by(name=query_emp_name).first()
            if query_emp_retrieved:
              print(f"Employee Found! \nID:{query_emp_retrieved.id}\nSalary: ${query_emp_retrieved.salary}\nLength of Employment: {query_emp_retrieved.length_of_employment}\nWarehouse: {query_emp_retrieved.warehouse_id}")
              break
            elif query_emp_name == "8":
              break
            else:
              print("Employee not found")
              continue
          
        elif seconday_input == "2":
          while True:
            query_ware_loc = input("Enter the name of wwarehouse (Case Sensitive) 8 to exit: ")
            query_wareloc_retrieved = session.query(Warehouse).filter_by(location=query_ware_loc).first()
            if query_wareloc_retrieved:
              print(f"Warehouse Found! \nLocation: {query_wareloc_retrieved.location}\nRevenue: ${query_wareloc_retrieved.revenue}\nSquare Feet: {query_wareloc_retrieved.sqft}")
              break
            elif query_ware_loc == "8":
              break
            else:
              print("Warehouse not found")
              continue
            
        elif seconday_input == "8":
          break
        else:
          print("Please enter a input of 1, 2 or 8")
    elif usr_input == "6":
      print("pressed 6")
    elif usr_input == "7":
      print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
      print("░░░░░░░░░░▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄░░░░░░░░░")
      print("░░░░░░░░▄▀░░░░░░░░░░░░▄░░░░░░░▀▄░░░░░░░")
      print("░░░░░░░░█░░▄░░░░▄░░░░░░░░░░░░░░█░░░░░░░")
      print("░░░░░░░░█░░░░░░░░░░░░▄█▄▄░░▄░░░█░▄▄▄░░░")
      print("░▄▄▄▄▄░░█░░░░░░▀░░░░▀█░░▀▄░░░░░█▀▀░██░░")
      print("░██▄▀██▄█░░░▄░░░░░░░██░░░░▀▀▀▀▀░░░░██░░")
      print("░░▀██▄▀██░░░░░░░░▀░██▀░░░░░░░░░░░░░▀██░")
      print("░░░░▀████░▀░░░░▄░░░██░░░▄█░░░░▄░▄█░░██░")
      print("░░░░░░░▀█░░░░▄░░░░░██░░░░▄░░░▄░░▄░░░██░")
      print("░░░░░░░▄█▄░░░░░░░░░░░▀▄░░▀▀▀▀▀▀▀▀░░▄▀░░")
      print("░░░░░░█▀▀█████████▀▀▀▀████████████▀░░░░")
      print("░░░░░░████▀░░███▀░░░░░░▀███░░▀██▀░░░░░░")
      print("░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░")
    elif usr_input == "8":
      print("Cya later aligator :)")
      break
    else:
      print("Please enter a number: 1 - 8")
   
    