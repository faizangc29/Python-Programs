# write a program for facatorial

n = int(input("enter a number: "))
p = 1


for i in range(1, n+1):
    p = p * i

print(f"the factor of {n} is {p}")    

