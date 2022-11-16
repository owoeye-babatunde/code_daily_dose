# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.


def birthdayCakeCandles(candles):
    # Write your code here
    tallest_cand = max(candles)
    num_tallest = 0
    
    for candle in range(len(candles)):
        if candles[candle] == tallest_cand:
            num_tallest += 1
            
    return num_tallest

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
