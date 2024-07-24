#!/usr/bin/env python3 
#lib/testing/debug.py

from __init__ import CONN, CURSOR #imports the connection and cursor to interact with the database
from department import Department #import department class

import ipdb

Department.drop_table() #drops the department table if exists, start with fresh table each time we run script
Department.create_table() #class method creates new department table,attributes match class


#create department instances
payroll = Department.create("Payroll", "Building A, 5th Floor")
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor> object

hr = Department.create("Human Resources", "Building C, East Wing")
print(hr)  # <Department 2: Human Resources, Building C, East Wing>


#update instances
hr.name = 'HR'
hr.location = "Building F, 10th Floor"
hr.update()
print(hr)  # <Department 2: HR, Building F, 10th Floor>

print("Delete Payroll")
payroll.delete()  # delete from db table, object still exists in memory
print(payroll)  # <Department 1: Payroll, Building A, 5th Floor> still exists in memory

ipdb.set_trace() #breakpoint in code
