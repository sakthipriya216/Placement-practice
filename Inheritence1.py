class A:
    def __init__(self):
        print('A')
class B:
    def __init__(self):
        print('B')
class C(A,B):
    def hi(self):
        print('hi')
c1=C()

#output - A
