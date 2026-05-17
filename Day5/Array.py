#insert element in the array
arr=[]
n=int(input("Enter size: "))      
for i in range(n):
    arr.append(int(input("Enter no:")))      
key = int(input("Enter key element to insert: "))
loc = int(input("Enter location (index): "))      
arr.append(0)
for i in range(n, loc, -1):
    arr[i] = arr[i - 1]
arr[loc] = key
print("Array after insertion: ",arr)

