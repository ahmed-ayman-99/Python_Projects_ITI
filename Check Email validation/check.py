#check.py


def check(name,email):
    while True:
        try:
            if not name or not name.isalpha():
                raise ValueError
            break
        except ValueError:
            print("Please enter a valid name(non-empty and not an integer).")
    while True:
        try:
            username,domain = email.split("@")
            if username and domain:
                x,y = domain.split(".")
                if x and y:
                    return (f"name: {name}",f"your email is: {email}")
                else:
                    return False
            else:
                return False
        except ValueError: 
            return False 


