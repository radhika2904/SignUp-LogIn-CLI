#login credentials
import csv

varFile = open("UserCreds.csv", "r")
file =  csv.reader(varFile)

login = False

print("enter login credentials")
a = input()
b = input()

for row in file:
    if row[0] == a and row[1] == b:
        login = True
        break
    else: 
        login = False

if login == True:
    print("login successful")
else: 
    print("login failed")

