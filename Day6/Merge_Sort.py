#Merge sort with sorted List

class MergeSort:
    def mergeSort(self, arr1, arr2):
        arr3=[]
        i=0
        j=0
        k=0
        while i<len(arr1) and j<len(arr2):
            if arr1[i]<arr2[j]:
                arr3.append(arr1[j])
                i+=1
                k+=1
            else:
                arr3.append(arr2[j])
                j+=1
                k+=1
        while len(arr1)>i:
            arr3.append(arr1[i])
            i+=1
            k+=1
        while len(arr2)>j:
            arr3.append(arr2[j])
            j+=1
            k+=1

        return arr3

if __name__ == '__main__':
    obj=MergeSort()
    arr1=[1,3,5,7,9]
    arr2=[2,4,6]
    ans=obj.mergeSort(arr1, arr2)
    print(ans)
        


#merge sort (Actual Code)[Unsorted list]
#The idea of merge sort is:
#divide the list into smaller parts
#sort each smaller part
# merge them back



#Merge sort with unsorted array


class MergeSort:
    def mergeSort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            arr1=arr[:mid]
            arr2=arr[mid:]
            self.mergeSort(arr1)
            self.mergeSort(arr2)
            i=0
            j=0
            k=0
            while i<len(arr1) and j<len(arr2):
                if arr1[i]<arr2[j]:
                    arr[k]=arr1[i]
                    i+=1
                    k+=1
                else:
                    arr[k]=arr2[j]
                    j+=1
                    k+=1
            while len(arr1)>i:
                arr[k]=arr1[i]
                i+=1
                k+=1
            while len(arr2)>j:
                arr[k]=arr2[j]
                j+=1
                k+=1

if __name__ == '__main__':
    obj=MergeSort()
    arr=[1,7,12,3,6,2,9]
    obj.mergeSort(arr)
    print(arr)
        






















     
