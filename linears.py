
def linears(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
        
    flag=1
    count=0
    for i in range(n):
        count+=1
        if(x==element[i]):
            flag=1
            print("found my element at ",str(i)," position")
            break;
        else:
            flag=0
    if flag==0:
        print("didnt find element")
    print(element)
    print("no. of iterations: ",count)