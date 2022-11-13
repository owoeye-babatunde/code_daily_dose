def diagonalDifference(arr):
    # Write your code here
    sum1 = 0
    sum2 = 0
    for n in range(len(arr)):
        sum1 += arr[n][n]
        sum2 += arr[n][(len(arr)-1)-n]
    
    return abs(sum1-sum2)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
