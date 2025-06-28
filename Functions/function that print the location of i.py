#using function that print the location of "i" character

def LocationOfi (x):
    for i in range (0,5):
     if x[i] == "i":
        return(i)
z=LocationOfi("messi")
print(z)
