# ============================================================
# CDPC DSA Training – Day 3 Assignment
# Topic: Functions & Searching Algorithms
# Language: Python
# ============================================================


# ------------------------------------------------------------
# Function: Without Parameters
# ------------------------------------------------------------
"""
def add():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    res = a + b
    print("Addition is ", res)

if __name__ == '__main__':
    add()
"""


# ------------------------------------------------------------
# Function: With Parameters (No Return Value)
# ------------------------------------------------------------
'''
def add(a, b):
    res = a + b
    print("Addition is: ", res)

if __name__ == '__main__':
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    add(a, b)
'''


# ------------------------------------------------------------
# Function: With Parameters & Return Value
# ------------------------------------------------------------
'''
def add(a, b):
    res = a + b
    return res

if __name__ == '__main__':
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    r = add(a, b)
    print("Addition is ", r)
'''


# ------------------------------------------------------------
# Function: Return Multiple Values
# ------------------------------------------------------------
def add(a, b):
    res1 = a + b
    res2 = a - b
    res3 = a * b
    return res1, res2, res3

if __name__ == '__main__':
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    r1, r2, r3 = add(a, b)
    print("Addition is ", r1)
    print("Subtraction is ", r2)
    print("Multiplication is ", r3)


# ------------------------------------------------------------
# Linear Search Algorithm
# ------------------------------------------------------------
def linear_search(n, arr, target):
    flag = False
    for i in range(n):
        if target == arr[i]:
            flag = True
            loc = i

    if flag:
        print("Search is successful and present at", loc)
    else:
        print("Search is Unsuccessful")

if __name__ == '__main__':
    n = int(input("Enter size: "))
    arr = []
    for i in range(n):
        arr.append(int(input()))
    target = int(input("Enter number to search: "))
    linear_search(n, arr, target)


# ------------------------------------------------------------
# Binary Search Algorithm
# ------------------------------------------------------------
def binary_search(n, arr, target):
    low = 0
    high = n - 1
    flag = False

    while low <= high:
        mid = (low + high) // 2
        if target == arr[mid]:
            flag = True
            loc = mid
            break
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    if flag:
        print("Search is successful and present at", loc)
    else:
        print("Search is Unsuccessful")

if __name__ == '__main__':
    n = int(input("Enter size: "))
    arr = []
    for i in range(n):
        arr.append(int(input()))
    target = int(input("Enter number to search: "))
    binary_search(n, arr, target)
