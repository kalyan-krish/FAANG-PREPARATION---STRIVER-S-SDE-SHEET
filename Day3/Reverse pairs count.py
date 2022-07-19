# Brute force approach
'''
493. Reverse Pairs
Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].

 

Example 1:

Input: nums = [1,3,2,3,1]
Output: 2
Example 2:

Input: nums = [2,4,3,5,1]
Output: 3

'''

class Solution:
    def reversePairs(self, nums):
        count = 0
        for i in range(len(nums)):
            for j in range(1,len(nums)):
                if i >= 0 and i < j and j < len(nums):
                    if nums[i] > 2 * nums[j]:
                        count += 1
        
        return count

s = Solution()
print(s.reversePairs([1,3,2,3,1]))

        