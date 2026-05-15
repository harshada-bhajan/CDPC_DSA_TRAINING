#program to reverse the number
no=int(input("Enter no: "))
n1=no%10 
no=no//10 
n2=no%10 
no=no//10 
n3=no%10 
rev=n1*100+n2*10+n3*1
print(rev)
