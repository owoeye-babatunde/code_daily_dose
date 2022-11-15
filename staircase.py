# The function accepts INTEGER n as parameter.


def staircase(n):
    # Write your code here
    s = ' '
    
    for i in range(1, n+1):
        space = s * (n-i)
        ash = '#' * i
        
        print(space + ash)
if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
