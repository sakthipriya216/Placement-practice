from random import shuffle
def get_input():
    x=-1
    while x not in ['0','1','2']:
        x=(input("Pick up the number 0,1 or 2: "))
    return int(x)
    
def check_game(l,input1):
    if l[input1] == 'O':
        print("Yes, Correct!!")
    else:
        print("Better luck next time!")
        print(l)

l=['O', ' ', ' ']
input1 = get_input()
shuffle(l)
check_game(l,input1)
