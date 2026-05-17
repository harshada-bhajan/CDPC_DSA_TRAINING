#Check for valid Palindrome String:
s="A man, a plan, a canal: Panama"
str=""
for x in s:
    if x.isalpha():
        str+=x.upper()
if str==str[::-1]:
    print("valid Palindrome")
else:
    print("invalid palindrome")


