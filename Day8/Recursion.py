#Factorial using Recursion
'''
def fact(n=1):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

if __name__ == '__main__':
    n=5
    res=fact(n)
    print(res)
'''        

#Multiply two numbers using recursion
"""
def multiply(x,y):
    if y==1:
        return x
    elif x==1:
        return y
    elif x==0 or y==0:
        return 0
    else:
        return x+multiply(x,y-1)
    
if __name__ == '__main__':
    x=2
    y=3
    res=multiply(x,y)
    print(res)
"""


#Find power using recursion
'''
def power(x,y):
    if x==1:
        return 1
    elif y==1:
         return x
    elif x==0:
        return 0
    elif y==0:
        return 1
    else:
        return x*power(x,y-1)
    
if __name__ == '__main__':
    x=2
    y=3
    res=power(x,y)
    print(res)
'''
#Find sum of Natural numbers using recursion
'''
def sum(n):
    if n==1:
        return 1
    elif n==0:
        return 0
    else:
        return n+sum(n-1)
    
if __name__ == '__main__':
    n=10
    res=sum(n)
    print(res)
'''


#fibonacci  series using recursion
'''
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

if __name__ == '__main__':
    n=10
    for x in range(n):
        print(fibo(x),end=" ")
'''

#permutation combinations 

'''
from itertools import permutations

def generate_permutations(num1,num2):
    number_str=str(number)
    perm=permutations(number_str)
    perm_list=["join(p)for p in perm"]
    return perm_list
'''


#case study(TCS)

from itertools import permutations

def generate_permutations(num1, num2):
    number_str = str(num1)
    perm = permutations(number_str)

    perm_list = []
    for p in perm:
        value = int("".join(p))
        if value > num2:
            perm_list.append(value)

    return perm_list


if __name__ == '__main__':
    num1 = 459
    num2 = 500

    res = generate_permutations(num1, num2)
    print(res)











