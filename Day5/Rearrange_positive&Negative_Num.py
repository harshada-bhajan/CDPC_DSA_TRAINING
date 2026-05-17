#Rearrange Positive and Negative numbers
arr = [-1, 2, -3, 4, 5, -6]
pos = []
neg = []
for i in arr:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
result = []
for i in range(len(neg)):
    result.append(neg[i])
    result.append(pos[i])
if len(pos) > len(neg):
    result.append(pos[-1])

print(result)
