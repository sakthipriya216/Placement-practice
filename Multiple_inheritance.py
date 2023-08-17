class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def flirt(self):
        print("I can flirt")
    def work(self,msg):
        print(msg)
        
class Boy(Human, Male):
    pass
        
b = Boy()
b.work() # op= I can work
b.work("Hello")
''' output Ln 17
ERROR!
Traceback (most recent call last):
  File "<string>", line 16, in <module>
TypeError: Human.work() takes 1 positional argument but 2 were given '''
        
