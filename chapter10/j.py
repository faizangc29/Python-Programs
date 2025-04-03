# def sum(a,b):
#     s = a+b
#     return s
# res = sum(1,4)
# print(res)
# n = 3
# for i in range(1,11):
#     print(f"{n} X {i} = {n*i}")
def fac(n):
    if(n==1):
        return 1
    return fac(n-1) * n

print(fac(5))