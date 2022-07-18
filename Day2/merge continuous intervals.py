'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

problem solving steps:
1. sort the nested list in increasing order by first element
2. Place the first index list in output list and start iteration from index 1 to end
3. store the prev element last index in lastend
4. compare start <= lastend if yes replace prev element lastelement to max of lastend or end
5. else store in output list and return 
 '''
# example [[2,4],[1,3]] comments for 1st iteration
def merge(intervals):
    intervals.sort(key = lambda i: i[0]) # sort by start value for nested list result = [[1,3],[2,4]]
    output = [intervals[0]]  # [[1,3]]

    for start,end in intervals[1:]: #start = 2,end = 4
        lastend = output[-1][1] # lastend = 3

        if start <= lastend: #2 <= 3
            output[-1][1] = max(lastend,end) # max(3,4)

        else:
            output.append([start,end])
        
    return output


print(merge(
[[1,3],[2,6],[8,10],[15,18]]))