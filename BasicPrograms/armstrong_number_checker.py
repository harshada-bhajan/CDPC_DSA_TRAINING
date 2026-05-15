#Check Number is Armstronge or not
no=int(input("Enter no: "))
sum=0
save=no

count=0
while no>0:
    no=no//10
    count=count+1
no=save

while no>0:
    rem=no%10
    sum=sum+(rem**count)
    no=no//10

if sum==save:
     print("no is armstronge")
else:
     print("no is not armstronge")
