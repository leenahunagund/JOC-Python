
import random

def choose():
    words=["hello","sunny","hammer","newyork","brisbane","doughnut","newhampshire"]
    pick=random.choice(words)
    return pick

def jumble(word):
     jumbled="".join(random.sample(word,len(word)))
     return jumbled

def thank(p1name,p2name,p1p,p2p):
    print(p1name,"your score is :",p1p)
    print(p2name,"your score is :",p2p)
    print("thanks for playing , have a nice day")
    
    
    
def play():
    p1name=input("enter player 1 name: ")
    p2name=input("enter player 2 name: ")
    p1p=0
    p2p=0
    turn=0
    while(1):
        #computers task
        word=choose()
        #create question
        qn=jumble(word)
        print(qn)
        #player 1
        if turn%2==0:
            print(p1name+" your turn")
            ans=input("what is on my mind ")
            if word==ans:
                print("yes "+p1name+" is right")
                p1p=p1p+1
                print("your score is :",p1p)
            else:
                print("better luck next time, i thought of "+word)
            c=input("1 to continue , 0 to exit:")
            c=int(c)
            if c==0:
                thank(p1name,p2name,p1p,p2p)
                break
        #player 2
        else:
            print(p2name +" your turn")
            ans=input("what is on my mind ")
            if word==ans:
                print("yes "+p2name+" is right")
                p2p=p2p+1
                print("your score is :",p2p)
            else:
                print("better luck next time, i thought of "+word)
            c=input("1 to continue , 0 to exit:")
            c=int(c)
            if c==0:
                thank(p1name,p2name,p1p,p2p)
                break
        turn=turn+1
play()
       
        
                
                
                
