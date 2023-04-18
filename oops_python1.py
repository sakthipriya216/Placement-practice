class Computer:
    
    #initialise the variables using __init__ method
    def __init__(self, cpu,ram):
        self.cpu=cpu
        self.ram=ram
    # config method in Computer class
    def config(self):
        print("config method")
        print(self.cpu,self.ram)

comp1=Computer("i5",6)
comp2=Computer("i6",8)

comp1.config()
comp2.config()
