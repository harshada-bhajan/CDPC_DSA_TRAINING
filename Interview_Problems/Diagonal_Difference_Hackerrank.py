#Diagonal Difference codde in Hackerank

def diagonalDifference(arr):
    n=len(arr)
    sum1=0
    sum2=0
    
    for i in range(n):
        sum1=sum1+arr[i][i]
        sum2=sum2+arr[i][n - 1 - i]

    return abs(sum1 - sum2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
