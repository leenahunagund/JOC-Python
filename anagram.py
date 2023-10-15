str1=input("input 1st word : ")
str2=input("input 2nd word : ")

print(sorted(str1))
print(sorted(str2))

if(sorted(str1)==sorted(str2)):
    print("anagram!")
else:
    print("not anagram")