#using funtion to generate the multiplication table in a list

table=[]
def listmultiply (x):
    for i in range(1,x+1):
        multiplication_table =[]
        for j in range(1,x+1):
            if i == j:
                multiplication_table.append(i*j)
                break
            multiplication_table.append(i*j)
        table.append(multiplication_table)
    return(table)
z=listmultiply(5)
print(z)