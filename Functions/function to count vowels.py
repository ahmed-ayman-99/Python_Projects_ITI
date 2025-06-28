# using function to count vowels:

def countvowels(x):
    count = 0
    for i in x:
        vowels = ["a","e","i","o","u"]
        if i in vowels:
            count += 1
    return count
z= countvowels("continue")
print(z)
