#using function to check if user entered his name not integer/empty

def check (name,email):
    while not name.isalpha():
        name = input("enter your vaild name: ")
    while not email.isalpha():
        email= input("Invalid e-mail. Please enter your correct e-mail: ")
    return (f"you are {name} and your e-mail is {email}")
z=check("ahmed","ahmed")
print(z)
