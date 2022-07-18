'''

You are given a read only array of n integers from 1 to n.

Each integer appears exactly once except A which appears twice and B which is missing.

Return A and B.

Note: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Note that in your output A should precede B.

Example:

Input:[3 1 2 5 3] 

Output:[3, 4] 

A = 3, B = 4

Problem solving steps:
1.Get the repeated element in list by sorting and comparing prev and current element
2.Get the missing element by sumN - sum(list) + repeated element i.e;
              ex : x+y+z = 10 (sum of 3 elements from formula)
                   x+x+z = 5 (sum of list given) 
                   with substraction y-z = 5 here y is the missing value z is repeating value 
                   so missing y = 5 + z
3. return the results.



'''
class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def repeatedNumber(self, A):
        A = list(A)
        A.sort()
        
        for i in range(len(A)):# step 1
            if A[i] == A[i-1]:
                repeat = A[i]
        
        n = len(A)
        
        sumN = n*(n+1)//2 #step2
        
        missing = abs((sumN-sum(A)) + repeat)
        
        return repeat,missing

s = Solution()
print(s.repeatedNumber([1,2,4,5,6,2]))