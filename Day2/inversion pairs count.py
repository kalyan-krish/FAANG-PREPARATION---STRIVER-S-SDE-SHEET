# Brute force approach

'''
For a given integer array/list 'ARR' of size 'N' containing all distinct values, find the total number of 'Inversions' that may exist.
An inversion is defined for a pair of integers in the array/list when the following two conditions are met.
A pair ('ARR[i]', 'ARR[j]') is said to be an inversion when:

1. 'ARR[i] > 'ARR[j]' 
2. 'i' < 'j'

Where 'i' and 'j' denote the indices ranging from [0, 'N').

Sample Input 1 :
3
3 2 1
Sample Output 1 :
3
Explanation Of Sample Output 1:
We have a total of 3 pairs which satisfy the condition of inversion. (3, 2), (2, 1) and (3, 1).

'''

from sys import *

def getInversions(arr, n) :
    count = 0
    for i in range(n):
        for j in range(1,n):
            if arr[i] > arr[j] and i < j:
                count += 1
    return count

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))