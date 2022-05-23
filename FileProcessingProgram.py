#Assignment 10.1 File Processing Program
#Austin Miller

from genericpath import isdir
import os #importing os library

import logging #importing logging

import os.path

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

D1 = input("Directory path to save file in:") #Asking for directory

while True:
    isdir = os.path.isdir(D1)
    if isdir is True:
        print("Directory exists!")
    elif isdir is False:
        print("Error with directory, or it does not exist, please run the program again with a correct directory.")
        exit()  
    break

os.chdir(D1)

file_name = input(str("Enter what you would like the file to be named:"))

name = input("Enter Your name:")

address = input("Enter Your address:")

phone = input("Enter your phone number:")

x = name, address, phone

y = open(file_name, 'w')
y.write(str(x))


f = open(file_name,'r')
f.read()
print(f.readline())
input('Thank you for using the program, press any key to close!')
exit()