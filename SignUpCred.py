#login cred
import csv
from getpass import getpass
from getpass import getuser

print("enter counter for sign up")
T = int(input())


while(T>0):
    varFile = open("UserCreds.csv", "a", newline = "")
    file = csv.writer(varFile)

    #file.writerow(["Username", "Password"])

    print("Enter username and password")
    a = input("Username:")
    b = getpass("Password:")

    file.writerow([a, b])
    print("Sign Up successful")
    T = T-1
