
# Brute force approach time complexity O(m*n)
from numpy import true_divide


def searchMatrix(matrix, target):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == target:
                return 'true'
            else:
                return 'false'

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 13

#print(searchMatrix(matrix,target))

#  Optimal approach of O(mlogn) complexity

def binarysearch(l,target):
    low = 0
    high = len(l)-1

    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if l[mid] == target:
            return True

        # Search the left half
        elif l[mid] > target:
            return binarysearch(l[low:mid], target)

        # Search the right half
        else:
            return binarysearch(l[mid+1:high+1], target)

    else:
        return -1

def searchmat(matrix,target):
    for i in range(len(matrix)):
        res = binarysearch(matrix[i],target)
        if res == True:
            return True
        else:
            continue
    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 67

print(searchmat(matrix,target))