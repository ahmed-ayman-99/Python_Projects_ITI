#using function to fill array given by the user and sort it 

numbers=[]
descending_order=[]
ascending_order=[]
def order(*x):
    for i in range (0,6): 
        numbers.append(x[i])
        ascending_order = sorted(numbers)
        descending_order = sorted(numbers,reverse=True)
        if i==4:
            break
    return (numbers),(ascending_order),(descending_order)
z=order(2,9,6,3,7)
print(z)
