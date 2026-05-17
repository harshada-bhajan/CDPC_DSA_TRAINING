#Reverse a String without inbuild function & shortcut:
str1="hello"
str2=""
for i in range(len(str1)-1,-1,-1):
    str2=str2+str1[i]
print("String Before Reverse:", str1)
print("String After Reverse:", str2)


#reverse String
s="Harshada"
rev=""
for x in s:
    rev=x+rev
print(rev)
