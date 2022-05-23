#Assignment 10.1 File Processing Program
#Austin Miller

import os #importing os library

import logging #importing logging

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

logging.basicConfig(filename='test.log', level=logging.DEBUG, format='%(asctime)s:')

D1 = input("Directory path to save file in:") #Asking for directory

while True:
    if not os.path.exists(D1):
        print("some error message")
        continue
    if not os.path.isdir(D1):
        print("another error message")
        continue
    break
print("Directory exists!")

file_name = input("Enter what you would like the file to be named:")

name = input("Enter Your name:")

address = input("Enter Your address:")

phone = input("Enter your phone number:")

x = name, address, phone
y = open(D1, 'w')
y.write(x)

open(D1)