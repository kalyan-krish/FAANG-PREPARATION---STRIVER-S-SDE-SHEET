
'''
1. sort the list and compare the prev and current item and return the current element as it is duplicate element

'''



class Solution:
    def findDuplicate(self, nums):
        
        nums.sort()
        
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]

'''
Problem solving steps:
1. Find duplicate element in the list.
2. Traversal through the list of elements in 1 -> n range
3. Assign negative signs for non repeating elements
4. if found negative element before the assignation in 2nd time that is the repeating element

'''
        

def findDuplicate(nums):
        
        for i in range(len(nums)):
            x = abs(nums[i])-1 # gives the correct index of element needs to be there
            if nums[x] < 0:
                repeat = x+1
                break
            else:
                nums[x] *= -1 # assign negative signs for all non repeating elements
        
        
        return repeat

print(findDuplicate([3,1,3,4,2]))