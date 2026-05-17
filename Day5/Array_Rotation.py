#Array Rotation
arr=[1, 2, 3, 4, 5]
k=2
for i in range(k):
    new=arr[-1]
    for j in range(len(arr)-1, 0, -1):
        arr[j]=arr[j-1]
    arr[0]=new
print("Array After Rotation: ",arr)
