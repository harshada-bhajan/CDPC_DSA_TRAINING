"""
CDPC DSA Training - Day 1
Topic: Array List in Python
"""

# -------------------------------
# 1. Creating List
# -------------------------------

ls = list()
print(type(ls))

ls = [1, 2, 3, 34, 77, 88]
print(type(ls))


# -------------------------------
# 2. Traversing in Array List
# -------------------------------

arr = [11, 22, 33, 44, 55, 66, 77, 88]
print(arr)

# Using index
for i in range(len(arr)):
    print(arr[i], end=" ")

print()

# Using direct element access
for x in arr:
    print(x, end=" ")


# -------------------------------
# 3. Indexing in List
# -------------------------------

arr = [11, 22, 33, 44, 55, 66, 77, 88]
print(arr[3])    # Positive indexing
print(arr[-1])   # Negative indexing


# -------------------------------
# 4. Slicing in List
# -------------------------------

arr = [11, 22, 33, 44, 55, 66, 77, 88]
print(arr[1:5])
print(arr[4:6])
print(arr[:6])
print(arr[4:])
print(arr[:])
print(arr[::1])
print(arr[::2])
print(arr[::3])
print(arr[::-1])
print(arr[::-2])


# -------------------------------
# 5. Finding Maximum of 3 Numbers
# -------------------------------

n1 = 10
n2 = 20
n3 = 30

max_val = n1
if max_val < n2:
    max_val = n2
if max_val < n3:
    max_val = n3

print(max_val)


# -------------------------------
# 6. Finding Max and Min in Array
# -------------------------------

arr = [5, 3, 9, 2, 8]

max_val = arr[0]
for i in range(1, len(arr)):
    if max_val < arr[i]:
        max_val = arr[i]
print(max_val)

min_val = arr[0]
for i in range(1, len(arr)):
    if min_val > arr[i]:
        min_val = arr[i]
print(min_val)


# -------------------------------
# 7. Removing Duplicate Elements
# -------------------------------

arr = [3, 2, 3, 1, 2, 4]
ans = []

for x in arr:
    if x not in ans:
        ans.append(x)

print(ans)
