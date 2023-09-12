
with open("file1.txt","r+") as myfile:
    print(myfile.read())
    myfile.write("i am fine")
myfile.close()
# r, w , a , r+
