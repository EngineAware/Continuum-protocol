#Exercise
#Write a program:
#1. ask for age
#2.If age >=18,print "Adult"
#3.If age <,print "Minor"

age=int(input("age:"))

if age >= 18:
    print("Adult")
if age < 18:
    print("Minor")

#create a login system:
#1.Ask for a username.
#if username is "admin"-> print "Access granted"

Username=input("Username:".strip())

if Username =="Admin":
    print("Access granted")