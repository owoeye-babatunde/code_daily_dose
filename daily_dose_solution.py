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
    arr1 = arr.copy()
    arr2 = arr.copy()
    arr1.remove(max(arr))
    arr2.remove(min(arr))
    print(sum(arr1), sum(arr2))
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
