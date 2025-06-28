#using funtion to create reverse mario pyramid

def mario (x):
    for i in range(x):
        print(" " * (x) + "*" * (i+1))
        x -=1
    return ("end")
z=mario(6)
print(z)