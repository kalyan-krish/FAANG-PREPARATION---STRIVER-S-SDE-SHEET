# pascal traingle

'''
    Problem solving steps:
        1. Initialize first row to result res = [[1]]
        2. for next n-1 rows take temp = [0] + res[-1] + [0]
        3. for next row of length prev row length + 1
        4. append value of temp[j] + temp[j+1] to row
        5.append that row to res
        
'''
        

class Solution:
    def generate(self, numRows):
       
        res = [[1]]
        
        for i in range(numRows-1):
            temp = [0] + res[-1] + [0]
            
            row = []
            
            for j in range(len(res[-1])+1):
                
                row.append(temp[j]+temp[j+1])
            
            res.append(row)
        
        return res

s = Solution()
print(s.generate(6))


# print kth row of pascal triangle
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)


def kthRow(k):
    l =[]
    for i in range(0,k+1):
        res1 = fact(k)
        res2 = fact(k-i) * fact(i)
        l.append(res1//res2)
    
    return l


print(kthRow(1))

