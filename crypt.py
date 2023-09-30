import string
dict ={}
data=""
file=open("mlit.txt","w")
for i in range(len(string.ascii_letters)):
    dict[string.ascii_letters[i]]=string.ascii_letters[i-1]
print(dict)
with open("lit.txt") as f :
    while True:
        c=f.read(1)
        if not c:
            print("end of file")
            break
        if c in dict:
            data=dict[c]
        else:
            data=c
        print(data)
        file.write(data)
        print(data)
file.close()