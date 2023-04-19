class Student:
    
    school="sairam"
    #used to initialise the attributes of an object
    def __init__(self, m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
       
    #instance method    
    def avg(self):
        return self.m1+self.m2+self.m3 / 3
    
    #class method... used to perform operation with class variables
    # We need to have a decorator to mention that its a class method
    # for class method we have to use cls keyword as a parameter
    
    @classmethod
    def get_school(cls1):
        return cls1.school
        
    #static methods.. It has nothing to do with class or instance variables
    #use decorator
    
    @staticmethod
    
    def info():
        print("heyyy")
        return 2;
    
s1=Student(10,20,30)
s2=Student(40,50,60)
print(s1.avg())
print(s2.avg())
print(s1.get_school())
print(Student.get_school())
print(Student.info())
print(s2.info())
s1.info()
