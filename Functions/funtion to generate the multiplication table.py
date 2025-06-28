#using funtion to generate the multiplication table

def multiply (x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            if i == j:
                print(f"{i}*{j} = {i*j}")
                break
            print(f"{i}*{j} = {i*j}")
    return ("end")
z=multiply(5)
print(z)