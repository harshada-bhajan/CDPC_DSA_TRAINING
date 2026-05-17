#If Else If Ladder

per=75
if per>=40and per<=60:
    print("Take admissioon in ABC college")
elif per>=61 and per<=80:
     print("Take admissioon in XYZ college")
elif per>=81 and per<=100:
     print("Take admissioon in PQR college")



#If Else
cp=int(input("Enter cost price: "))
st=input("Are you student yes/no")
if st=="yes":
    if cp>500:
        ds=cp*0.10
    else:
        ds=cp*0.05
else:
    if cp>500:
        ds=cp*0.08
    else:
        ds=cp*0.02
net=cp-ds


#For Loop

import numpy as np;
for i in range(1,6):
    print(i)

for i in range(1,11):
    print(i)
    
for i in range(1,11,3):
    print(i)


for i in range(10,0,-2):
    print(i)


arr=[1,2,3,4,5,5]
for i in range(len(arr)):
    print(arr[i])

for x in arr:
    print(x)


for i in range(1,11):
    if i==5:
        continue
    print(i)



#While Loop

i=1
j=10
while i<j:
    if i==3:
        i=i+1
        j=j-1
        continue
    print(i,"\t",j)
    i=i+1
    j=j-1
    
#Factorial Of Number using While Loop
import numpy as np
num=int(input("Enter a number: "))
fact =1
while num>0:
    fact*=num
    num-=1
print("Factorial=",fact)











    
