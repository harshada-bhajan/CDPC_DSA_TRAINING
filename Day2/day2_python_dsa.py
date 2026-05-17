# ============================================================
# CDPC DSA Training – Day 2
# Topics: Arrays, Lists, Tuples, Sets, Loops, Patterns,
#         Strings, Dictionary & Basic Problem Solving
# ============================================================

# -----------------------------------
# Array Traversing
# -----------------------------------

arr = [11, 22, 33]
print(arr)

for i in range(len(arr)):
    print(arr[i])
    
# -----------------------------------
# Nested Loop (2D Array / Nested List Traversing)
# -----------------------------------

arr = [[1, 2, 3], 22, [4, 5]]
print(arr)
for x in range(len(arr)):
    print(arr[x])

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(arr)
for x in range(len(arr)):
    print(arr[x])

for i in range(len(arr)):
    for j in range(len(arr[i])):
        print(arr[i][j], end=" ")
    print()


# -----------------------------------
# Tuple (Immutable Data Structure)
# -----------------------------------

t = ()
t = tuple()
t = (23, 24, 234, 234, 324, 45, 7)
print(type(t))

# -----------------------------------
# Set (Unordered & Unique Collection)
# -----------------------------------

# Empty set creation
s = set()
print(s)
print(type(s))

# Duplicate elements automatically removed
s = {1, 2, 3, 4, 5, 3, 2, 4, 3, 2, 4, 4}
print(s)

# Removing duplicates from list using set
arr = [1, 2, 3, 4, 5, 3, 2, 4, 3, 2, 4, 4]
s = set(arr)
arr = list(s)
print(arr)

# -----------------------------------
# List: User Input & Printing Elements
# -----------------------------------

n = int(input("enter size: "))
print("Enter list element : ")
arr = []

for i in range(n):
    ele = int(input("enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    print(arr[i])


    
# -----------------------------------
# How to Take Input in Python
# -----------------------------------

# Single integer input
int(input())    # example input: 11

# Integer input stored in variable
a = int(input())
a = int(input())

# Two integers input using map
a, b = map(int, input().split())
a, b = map(int, input().split())

# List input using map
arr = list(map(int, input().split()))


# -----------------------------------
# Sum of List Elements
# -----------------------------------

n = int(input("Enter size: "))
print("Enter list element: ")
arr = []
sum = 0

for i in range(n):
    ele = int(input("Enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    sum = sum + arr[i]
    print(sum)
    
# -----------------------------------
# Sum of Even & Odd Numbers in List
# -----------------------------------

n = int(input("Enter size: "))
print("Enter list element: ")
arr = []
even = 0
odd = 0
e1 = 0
o1 = 0

for i in range(n):
    ele = int(input("Enter element: "))
    arr.append(ele)

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        even = even + arr[i]
        e1 = e1 + 1
    else:
        odd = odd + arr[i]
        o1 = o1 + 1

print(even)
print(odd)

# --------------------------
# Tech Number Program
# --------------------------

no = int(input("Enter no: "))
n1 = 0
n2 = 0
save = no
sum = 0
count = 0

while no > 0:
    no = no // 10
    count = count + 1

no = save

if count % 2 == 0:
    mid = count // 2

n1 = no % 10**mid
n2 = no // 10**mid

sum = n1 + n2
sq = sum * sum

if sq == no:
    print("no is tech number")
else:
    print("no is not tech number")

# -----------------------------------
# Nested Loop: Basic Patterns
# -----------------------------------

# Pattern 1: Same number in each row
for i in range(1, 5):
    for j in range(1, 5):
        print(i, end=" ")
    print()

print()

# Pattern 2: Continuous numbers
n = 1
for i in range(1, 5):
    for j in range(1, 5):
        print(n, end="\t")
        n = n + 1
    print()


# -----------------------------------
# Pattern Programs (ABCD, Numbers & Stars)
# -----------------------------------

# Pattern 1: Alphabet Pattern (ABCD...)
n = 65
for i in range(1, 5):
    for j in range(1, 5):
        print(chr(n), end="\t")
        n = n + 1
    print()

print()

# Pattern 2: Number Triangle
for i in range(1, 5):
    for j in range(1, i + 1):
        print(i, end="")
    print()

print()

# Pattern 3: Star Triangle (Increasing)
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print()

print()

# Pattern 4: Star Triangle (Decreasing)
for i in range(4, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

print()

# Pattern 5: Right Aligned Star Pattern
sp = 0
for i in range(4, 0, -1):
    for x in range(sp):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end="")
    print()
    sp = sp + 1

# -----------------------------------
# String Handling in Python
# -----------------------------------

# String creation
s = "harshu"
print(s)

s = 'harshada'
print(s)

# Multiline string
s = """kfbfvkdfjv
kbvdkfvbdfkvj
kjbvdfjbvfjv
kjvbkdfbv
lkbfvif"""
print(s)

# -----------------------------------
# String Reversal using Slicing
# -----------------------------------
s = "Harshada"
print(s[::-1])

# -----------------------------------
# String Searching Methods
# -----------------------------------
s = "Learning Python is very easy from Ashish sir"
print(s.find("Python"))   # 9
print(s.find("Java"))     # -1
print(s.find("r"))        # 3
print(s.rfind("r"))       # 43

# -----------------------------------
# String Count Method
# -----------------------------------
s = "abcabcabcabcadda"
print(s.count('a'))
print(s.count('ab'))
print(s.count('a', 3, 10))

# -----------------------------------
# String Replace Method
# -----------------------------------
s = "Learning python is very difficult from Ashish Sir"
s1 = s.replace("difficult", "easy")
print(s1)

# -----------------------------------
# String Split Method
# -----------------------------------
s = "Learning python is very difficult from Ashish Sir"
ls = s.split()
print(ls)
print(len(ls))

s = "22-02-2022"
ls = s.split("-")
print(ls)

s = "www.harshadabhajan.com"
ls = s.split(".")
print(ls)

# -----------------------------------
# String Join Method
# -----------------------------------
l = ['Nagpur', 'pune', 'Mumbai', 'Delhi']
s = '#'.join(l)
print(s)

l = ['Nagpur', 'pune', 'Mumbai', 'Delhi']
s = '|'.join(l)
print(s)

# -----------------------------------
# Reverse String using join & reversed
# -----------------------------------
s = input("Enter String: ")
print(':'.join(reversed(s)))

# -----------------------------------
# Program: Reverse Order of Words
# -----------------------------------
s = "Learning python is very difficult from Ashish Sir"
ls = s.split()
print(ls)
ls = ls[::-1]
print(ls)
s = " ".join(ls)
print(s)


# -----------------------------------
# Program: Reverse Each Word in String
# -----------------------------------
s = "Learning python is very difficult from Ashish Sir"
ls = s.split()
print(ls)
ans = ""
for x in range(len(ls)):
    ans = ans + ls[x][::-1] + " "
print(ans)


# -----------------------------------
# Program: Print Each Character of String
# -----------------------------------
s = "Learning python is very difficult from Ashish Sir"
print(s)
for x in range(len(s)):
    print(s[x])


# -----------------------------------
# Program: Remove Duplicate Characters
# -----------------------------------
s = "ABCDABBCDABBBCCCDDEEEF"
ans = ""
for x in s:
    if x not in ans:
        ans = ans + x
print(ans)


# -----------------------------------
# Program: Mobile Number Validation
# -----------------------------------
no = input("Enter mobile number: ")
if no.isdigit():
    if len(no) == 10:
        if no.startswith('6') or no.startswith('7'):
            print("Valid Mobile Number")
        else:
            print("Invalid Mobile Number")
    else:
        print("Invalid Mobile Number")
else:
    print("Please enter valid 10 digit mobile number")


# -----------------------------------
# Dictionary: Basic Example
# -----------------------------------
d = {}
d[100] = "ashish"
d[200] = "Prashant"
d[300] = "sandip"
print(d)


# -----------------------------------
# Dictionary: Student Record Input
# -----------------------------------
rec = {}
n = int(input("Enter number of students: "))
for i in range(n):
    name = input("Enter name: ")
    per = float(input("Enter percentage: "))
    rec[name] = per

print(rec)
for x in rec:
    print(x, "\t", rec[x])


# -----------------------------------
# Dictionary: Predefined Values
# -----------------------------------
d = {
    100: 'harshada',
    200: 'Jayu',
    300: 'khushi'
}
print(d)

