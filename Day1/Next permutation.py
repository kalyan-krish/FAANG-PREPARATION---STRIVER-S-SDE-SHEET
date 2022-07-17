# Next permutation of array/list

'''
Problem solving steps:
1. first get the peak element of list from end of list.
2. if list is in decreasing order arrange/sort in increasing order (in this case no permutation is possible).
3. special case in which if peak element+1 > peak element -1 and peak element +1 < peak element. in this case swap the peak element +1 and peakelement -1
4. normal case in which swap the last peak and before element.
'''

def nextpermutation(l):
    n = len(l)
    peak = -1
    # get the last peak element of the list from end.
    for i in range(n):
        if l[i] > l[i-1]:
            peak = i

    #check if elements in decending order if yes sort in ascending order
    if peak == -1:
        for i in range(0,n//2):
            l[i],l[n-i-1]=l[n-i-1],l[i]

    index = peak

    # check if last peak + 1 > last peak -1 and last peak + 1 < last peak if yes change the peak index
    for i in range(peak,len(l)):
        if l[i] > l[index-1] and l[i] <l[index]:
            index = i
        
    # swap the last peak and before element and sort the remaining elements after peak
    l[index],l[peak-1] = l[peak-1],l[index]
    l[peak:] = sorted(l[peak:])
    return l

l = [5,4,3,2,1]
print(nextpermutation(l))
