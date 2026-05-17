#intersection of two arrays

arr1=[1, 2, 2, 1]
arr2=[2, 2]
arr3=[]

for i in range(len(arr)):
    for j in range(len(arr2)):
        if arr1[i] == arr2[j]:
            if arr[i] not in arr3: 
                arr3.append(arr[i])
print(arr3)
