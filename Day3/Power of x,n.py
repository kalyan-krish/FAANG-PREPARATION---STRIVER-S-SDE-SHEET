# power of x of n

# brute force
def power(x,n):
    return x**n


# optimal approach
'''
problem solving steps:
1. for n iterations we have to mulitply to get power of x and n
2. but we can do x*x for n//2 iterations gives same result
3. if n is odd multiply result with x another 1 time
4. return res if n is positive or else return 1/res

'''
def power(x,n):
    if n == 0:
        return 1
    if x == 0:
        return 0

    res = power(x*x,n//2)

    if n%2:
        res = res * x
    
    else:
        res = res

    return res if n > 0 else 1/res

print(power(3.23432,2))