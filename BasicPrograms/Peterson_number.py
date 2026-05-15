#Check number Peterson or not
no=int(input("Enter no: "))
sum=0
fact=1
save=no
while no>0:
    rem=no%10
    fact=1
    while rem>0:
        fact=fact*rem
        rem=rem-1
        sum=sum+fact
        no=no//10
if save==sum:        
     print("no is peterson")
else:
     print("no is not peterson")
