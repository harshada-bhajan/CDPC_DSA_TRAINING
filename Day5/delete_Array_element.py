#delete element in the array
arr=[]
n=int(input("Enter size: "))      
for i in range(n):
    arr.append(int(input("Enter no: ")))      
loc = int(input("Enter location to delete: "))      
for i in range(loc+1, len(arr)):
    arr[i-1]=arr[i]
arr.pop()
print("Array after insertion: ",arr)
