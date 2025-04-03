# find a greater in three 

def greatest(a, b, c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a = int(input("enter a number: "))
b = int(input("enter a number: "))
c = int(input("enter a number: "))

g = (greatest(a, b, c))
print(f"Number is grater: {g}")