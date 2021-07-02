"""
Given a sorted array containing only 0s and 1s, find the transition point. 

The task is to complete the function transitionPoint() that takes array and N as input
parameters and returns the 0 based index of the position where "0" ends and "1" begins.
If array does not have any 1s, return -1. If array does not have any 0s, return 0.
"""


def transitionPoint(arr, n):
    if 1 not in arr:
        return -1
    
    elif 0 not in arr:
        return 0
    
    else:
        for i in range(n):
            if arr[i]==1:
                return i
