no=int(input("Enter no: "))
n1=no%10 #3
no=no//10 #12
n2=no%10 #2
no=no//10 #1
n3=no%10 #1
no=no//10
n4=no%10
no=no//10
n5=no%10
res =n1+n2+n3+n4+n5
print(res)
