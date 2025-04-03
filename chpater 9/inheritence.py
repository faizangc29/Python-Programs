class employe:
    def show(self):
        a = input("Enter your Name ")
        print(f"Name is  {a}")
class manger():
    def language(self):
        l = input("Enter yor language ")
        
        print(f"the language is {l}")
    
class final(employe, manger,):
    def salary(self):
            print("your salary is 100000")
         

    

f = final()
f.show()
f.language()
f.salary()