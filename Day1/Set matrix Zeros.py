class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.

        problem solving steps:
        1. Take first column and first row as reference column and row
        2. intialize a flag col1 = 1 and check if any element in column 0 are zero if yes update col1 = 0
        3. from column 1 check if any element is zero if zero update the corresponding reference column and row to zero
        4. Now from reverse check every element if it corresponding reference column or row has zero element update that to zero
        5. if col1 = 0 then update matrix every element in first column to zero
        """
        col1 = 1  
        for i in range(len(matrix)):
            if matrix[i][0] == 0: # step 2
                col1 = 0
            for j in range(1,len(matrix[0])):# step 3
                if matrix[i][j] == 0:
                        matrix[0][j] = 0
                        matrix[i][0] = 0
                
        for k in range(len(matrix)-1,-1,-1): # step 4
            for m in range(len(matrix[0])-1,0,-1):
                    if matrix[0][m] == 0 or matrix[k][0] == 0:
                        matrix[k][m] = 0
            
            if col1 == 0: # step 5
                matrix[k][0] = 0

        
        return matrix
                    
        

s = Solution()
print(s.setZeroes([[1,0,2,4],
             [2,1,0,3],
             [1,1,3,3]]))
