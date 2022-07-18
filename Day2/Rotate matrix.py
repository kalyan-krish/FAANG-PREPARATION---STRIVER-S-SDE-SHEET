'''
48. Rotate Image

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
 DO NOT allocate another 2D matrix and do the rotation.
Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


problem solving steps:
1. Rotate n x n matrix = Transpose of matrix + reverse/reflect

'''
# transpose + reflect method


class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                if i != j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        
        for k in range(len(matrix)):
            for h in range(len(matrix[0])//2):
                temp = matrix[k][h]
                matrix[k][h] = matrix[k][len(matrix[0])-h-1]
                matrix[k][len(matrix[0])-h-1] = temp
                
        return matrix


# Transpose + reverse              

def rotates(matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                if i != j:
                    temp = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = temp
        
        for k in range(len(matrix)):
            matrix[k].reverse()

        return matrix

matrix = [[1,2,3],[4,5,6],[7,8,9]]

print(rotates(matrix))