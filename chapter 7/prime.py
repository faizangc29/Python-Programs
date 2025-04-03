# write a program display prime number

n = int(input("enter a number:"))

for i in range(2, n):
    if(n%i)==0:
        print("Number is nor prime")
        break
else:
    print("Number is prime")    