# content1 = "Good Morning boys "
# content2 = "pthon course is the most good course and ready to try it"
# with open("new.txt", "w") as f:
 
#        f.write(content1)


# with open("new.txt", "a") as f:
#        f.write(content2)
with open("new.txt") as f:
    data = f.read()

if("boys" in data):
    print("data is find")
else:
    print("data is not find")    
    