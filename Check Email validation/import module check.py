import check as c

name= input("Enter yout first name: ")
email= input("Please enter your e-mail: ")

x=5
while not c.check(name,email):
    x -=1
    email= input("Please enter valid e-mail: ")
    if x == 0:
        print("Validation failed, you entered wrong email 5 times") 
        break 

z= c.check(name,email)
print(z)
