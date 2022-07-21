'''
62. Unique Paths

There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.

 Input: m = 3, n = 7
Output: 28
Example 2:

Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down

Problem solving steps using recursion:
1. if pointer reaches end of row and end of column count it 1 sucessful path
2. and you can go either right or down from current position
3. if you cross boundaries return 0
 

'''

def countpaths(i,j,n,m):
    if i == (n-1) and j == (m-1):
        return 1
    if i >= n or j >= m:
        return 0

    else:
        return countpaths(i+1,j,n,m) + countpaths(i,j+1,n,m)


def uniquepaths(a,b):
    return countpaths(0,0,a,b)


total = uniquepaths(2,3)
print(total)