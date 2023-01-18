# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 11:20:37 2022

@author: raulc
"""

from easyinput import read


# Iterative Binary Search Function
# It returns index of x in given array arr if present,
# else returns -1

# Precondition on arr, has to be sorted in ascending order
def binary_search_iter(arr, x):
    low = 0
    high = len(arr) - 1     # In python lists start from position 0
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2     # Gives the quotient - the remainder
 
        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
 
def binary_search_recursive(arr, low, high, x):     # Since it will be recursive need to specify boundaries which will change
 
    # Check base case
    if high >= low:
 
        mid = (high + low) // 2     # Gives the quotient - the remainder
 
        # If element is present at the middle itself
        if arr[mid] == x:
            return mid
 
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif arr[mid] > x:
            return binary_search_recursive(arr, low, mid - 1, x)
 
        # Else the element can only be present in right subarray
        else:
            return binary_search_recursive(arr, mid + 1, high, x)
 
    else:
        # Element is not present in the array
        return -1 
 