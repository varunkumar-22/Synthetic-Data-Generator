#Impoting Faker and Pandas
from faker import Faker
import pandas as pd
fake=Faker(locale="en_US")
#Synthetic Employee Data Generation
def create_employee_data(user_input):
    employee_list=[]
    for i in range(0,user_input):
        employee={}
        employee["Name"]=fake.name()
        employee["Job"]=fake.job()
        employee["department"]=fake.random_element("IT","Finance","Marketing","HR")
        employee["Email"]=fake.email()
        employee["Mobile_Number"]=fake.phone_number()
        employee["Salary"]=fake.random_int(min=20000,max=1600000,step=1000)
        employee_list.append(employee)
    print(pd.DataFrame(employee_list))
user=int(input("Enter the no. of empolyess: "))
create_employee_data(user)
