''' multiple of 3 - fizz
multiple of 5- buzz
multiple of 3,5 - fizzbuzz

while(1):
    n=input("enter any number :")
    n=int(n)
    if(n%3==0):
        if(n%5==0):
            print("fizzbuzz")
        else:
            print("fizz")
    elif (n%5==0):
        print("buzz") '''

for i in range(1,51):
    if(i%3==0):
        if(i%5==0):
            print(str(i),"= fizzbuzz")
        else:
            print(str(i)," = fizz")
    elif (i%5==0):
        print(str(i),"= buzz")
    else:
        print(str(i))
