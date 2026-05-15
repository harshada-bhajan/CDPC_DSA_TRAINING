#Calculate the factorial of number
no=int(input("Enter no: "))
fact=1
while no>0:
    fact=fact*no
    no=no-1
    
print(fact)
