#using function to Validate username and password in dic.

users = [{"name":"omar","password":123},{"name":"ahmed","password":456}]
def checkvalid(user_name,password):
    for i in users: 
        if user_name == i["name"]:
            if password == i["password"]:
                print("Acess Allowed")
                break
            else:
                password = input("enter the correct password: ")
        else:
            user_name = input("enter an authorized username: ")
    return ("end")
z=checkvalid("omar",123)
print(z)