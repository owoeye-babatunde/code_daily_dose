# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 06:20:37 2022

@author: BABATUNDE
"""

# MinMaxSum Hackerrrank
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    min_sum = arr.copy()
    max_sum = arr.copy()
    min_sum.remove(max(arr))
    max_sum.remove(min(arr))
    print(sum(min_sum), sum(max_sum))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
