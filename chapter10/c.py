num = []
class student:
    
    def marks(self):
       
        for i in range(0,10):
         a=int( input("enter marks") )
         num.append(a) 

    

    def grade(self):
     for i in range(0,10):
               if(num[i]>=50):
                  print("pass")
               else:
                  print("fail")
         

     
        
    
s = student()
s.marks()
s.grade()




   