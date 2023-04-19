class Student:
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.Laptop()
        
    def show(self):
        print(self.name,self.rollno)
        self.lap.show()
    
    #INNER CLASS 
    class Laptop:
        def __init__(self):
            self.brand='hp'
            self.ram=8
            
        def show(self):
            print(self.brand,self.ram)

s1=Student('Sakthi',26)
print(s1.lap.brand)
s1.show()
