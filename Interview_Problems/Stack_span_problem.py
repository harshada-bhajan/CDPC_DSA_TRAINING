price = [100,80,60,70,60,75,85]

N = 7

ans = [1]

for i in range(1, N):

    if price[i] < price[i-1]:
        ans.append(1)

    else:
        ans.append(2)

for i in range(N):

    if ans[i] == 2:
        print(2, end=" ")
    else:
        print(ans[i] ** 3, end=" ")
