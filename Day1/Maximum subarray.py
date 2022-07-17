'''
53. Maximum Subarray

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.
Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

problem solving steps:
1. Take first element as maxsub
2. traversal through list and sum the next element in loop to cursum and compare cursum and maxsum
3. if cursum is -ve intialize to 0.

'''
def maxSubArray(nums):
    maxsub = nums[0]
    cursum = 0

    for n in nums:
        if cursum < 0:
            cursum = 0
        
        cursum += n
        maxsub = max(maxsub,cursum)

    return maxsub

print(maxSubArray([1,-2,3,4]))

