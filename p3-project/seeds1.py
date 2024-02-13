import random
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from faker import Faker
from Inventory import *

if __name__ == "__main__":
  engine = create_engine('sqlite:///biztracker.db')
  Employee.__table__.drop(engine)
  Warehouse.__table__.drop(engine)
  Region.__table__.drop(engine)
  Base.metadata.create_all(engine)
  
  Session = sessionmaker(bind=engine)
  session = Session()
  fake = Faker()
  
  for _ in range(100):
    employee = Employee(name=fake.name(), 
                        salary= fake.random_int(min=40000, max=120000), 
                        length_of_employment= fake.random_int(min=1, max=120),
                        warehouse_id= fake.random_int(min=1, max=10)
                        )
    session.add(employee)
    session.commit()
  for _ in range(10):
    warehouse = Warehouse(location= fake.city(), 
                          sqft= fake.random_int(min=9000, max=40000), 
                          revenue= fake.random_int(min= 1500000, max= 5000000) 
                          )
    session.add(warehouse)
    session.commit()
  for _ in range(10):
    region = Region(employee_id=fake.random_int(min=1,max=100),
                    warehouse_id=fake.random_int(min=1,max=10),
                    total_employees=0)
    session.add(region)
    session.commit()
    #insert some logic to find the total number of employees then add/commit my session
  print("refreshed the board")
  session.close()