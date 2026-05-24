#Python Implementation of Hashing

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table=[]
        for i in range(size):
            self.table.append([])

    def hash_function(self, key):
        return key%self.size

    def insert(self, key):
        index=self.hash_function(key)
        self.table[index].append(key)

    def display(self):
        for x in range(10):
            print(self.table[x])

h=HashTable(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()




#Linear Probing

class LinearProbing:
    def __init__(self, size):
        self.size = size
        self.table=[None]*size

    def hash_function(self, key):
        return key%self.size

    def insert(self,key):
        index=self.hash_function(key)

        while self.table[index] is not None:
            index=(index+1)%self.size
            
        self.table[index]=key
         
    def display(self):
        print(self.table)

h=LinearProbing(10)
h.insert(15)
h.insert(25)
h.insert(35)
h.display()




#Build Hash Table Manually

class MyHashTable:
    def __init__(self, size):
        self.size = size
        self.table=[[] for _ in range(size)]

    def hash_function(self, key):
        return key%self.size

    def insert(self,key, value):
        index=self.hash_function(key)
        self.table[index].append((key, value))

    def search(self, key):
        index= self.hash_function(key)
        for k,v in self.table[index]:
            if k==key:
                return v
        return "Not found"
    
    def delete(self, key):
        index= self.hash_function(key)

        for i, (k, v) in enumerate(self.table[index]):
            if k== key:
                del self.table[index][i]
                return
            
    def display(self):
        print(self.table)

h=MyHashTable(10)
h.insert(1, "Ashish")
h.insert(11, "Rahul")

print(h.search(11))

h.display()
h.delete(11)
h.display()





#Two sum problem using Hashing Technique

class Solution:
    def twoSum(self, nums: List[int], target: int)-> List[int]:
        hash_map ={}

        for i in range(len(nums)):
            current_num = nums[i]
            complement = target-current_num
            if complement in hash_map:
                return[hash_map[complement], i]
            hash_map[current_num] = i


            

#two sum problem solved by me

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return(i ,j)




#Regular Expression

import re
count=0
pattern=re.compile("ab")
matcher=pattern.finditer("abaababaab")
#print(matcher)
for match in matcher:
    count+=1
    print(match.start(),'...',match.end(),'...',match.group())
print("total no of group occurances : ",count)




#pass pattern to finiter()

import re
count=0
#pattern=re.compile("ab")
#matcher=pattern.finditer("abaababaab")
matcher=re.finditer("ab","abaababaab")
for match in matcher:
    count+=1
    print(match.start(),'...',match.end(),'...',match.group())
print("total no of group occurances : ",count)





#find patterns

import re
#x="[abc]"
#x="[^abc]"
x="[a-z]"
#x="[0-9]"
#x="[a-zA-Z0-9]"
#x="[^a-zA-Z0-9]"
matcher=re.finditer(x,"a7bD2@k2$D8z")
for match in matcher:
    print(match.start(),'...',match.group())





#pre defined character classes:

import re
#x="\\s"
#x="\\S"
x="\\d"
#x="\\D"
#x="\\w"
#x="\\W"
#x="."
matcher=re.finditer(x,"a7b D 2@k2$D8z")
for match in matcher:
    print(match.start(),'...',match.group())





#Quantifiers

import re
#x="a"
#x="a+"
x="a*"
#x="a?"
#x="a{3}"
#x="a{2,3}"
matcher=re.finditer(x,"abaababaabaaabaaaa")
for match in matcher:
    print(match.start(),'...',match.group())





#Match Function

import re
str=input("Enter any String : ")
m=re.match(str, "abc@xyz_pqr*")
if m!=None:
    print("Yes matching is available at beg")
    print('start index: ',m.start(),'. end index:'.m.end())
else:
    print("matching is not available at beg")





#Full Match

import re
str=input("Enter any String : ")
m=re.fullmatch(str, "abcabcabc")
if m!=None:
    print("matching is available")
else:
    print("matching is not available")





#findall(): to find all occurances of the match.

import re
list=re.findall("[0-9]","ab4#hf7p@5qrs9")
print(list)
for x in list:
    print(x)
    




#Replacement

import re
str=re.sub("[a-z]","$","abfa@4bc_v5&bz")
print(str)
print(type(str))





#10 digit number
import re
number=input("Enter mobile number")
match=re.fullmatch("[6-9]\\d{9}",number)
if match!=None:
    print(number," is valid mobile number")
else:
    print(number," is not valid mobile number")
    

    
    
