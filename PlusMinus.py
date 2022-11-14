

# The function accepts INTEGER_ARRAY arr as parameter.


def plusMinus(arr):
    # Write your code here
    neg_k = sum([i < 0 for i in arr])
    pos_k = sum([i > 0 for i in arr])
    zero_k = sum([i == 0 for i in arr])
    
    print(round(pos_k/len(arr), 6)) 
    print(round(neg_k/len(arr), 6))
    print(round(zero_k/len(arr), 6))
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
