import random

# guess the movie name
movies=["jurrasic world","star wars","fast and furious","oceans8","devil wears prada","transformers"]
def createquestion(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if(letters[i]==' '):
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn
    
def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True
    
def unlock(qn,movie,letter):
     ref=list(movie)
     qn_list=list(qn)
     temp=[]
     n=len(movie)
     for i in range(n):
         if ref[i]==' ' or ref[i]==letter:
             temp.append(ref[i])
         else:
             if(qn_list[i]=='*'):
                 temp.append('*')
             else:
                temp.append(ref[i])
     qn_new=''.join(str(x) for x in temp)
     return qn_new
    
    
    
def play():
    p1name=input("player 1 input your name : ")
    p2name=input("player 2 input your name : ")
    pp1=0
    pp2=0
    turn=0
    willing=True
    while willing:
        if(turn%2==0):
            turn+=1
            #player 1 chance
            print(p1name," your turn")
            picked_movie=random.choice(movies)
            qn=createquestion(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=input("press 1 to guess the movie or 2 to unlock another letter")
                    if d=='1':
                        ans=input("your ans: ")
                        if ans==picked_movie:
                            pp1=pp1+1
                            print("correct")
                            not_said=False
                            print(p1name," score is : ",pp1)
                        else:
                            print("try again , wrong answer")
                else:
                    print(letter,"not found")
            c=input("press 1 to continue , 0 to quit")
            if(c=='0'):
                print(p1name," score is : ",pp1)
                print(p2name," score is : ",pp2)
                print("thanks for playing")
                print("have a nice day")
                willing=False
                
        else:
            #player 2 chance
            
            print(p2name," your turn")
            picked_movie=random.choice(movies)
            qn=createquestion(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=input("press 1 to guess the movie or 2 to unlock another letter")
                    if d=='1':
                        ans=input("your ans: ")
                        if ans==picked_movie:
                            print("correct")
                            pp2+=1
                            not_said=False
                            print(p2name," score is : ",pp2)
                        else:
                            print("try again , wrong answer")
                else:
                    print("not found")
            c=input("press 1 to continue , 0 to quit")
            if(c=='0'):
                 print(p1name," score is : ",pp1)
                 print(p2name," score is : ",pp2)
                 print("thanks for playing")
                 print("have a nice day")
          
                    
play()
