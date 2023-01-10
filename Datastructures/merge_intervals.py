def merge(intervals):
    intervals.sort(key = lambda x:x[0])
    #print(intervals)
    res = [intervals[0]]

    for start, end in intervals[1:]:   #for 1st iteration start=1 and end=3.
        last_end = res[-1][1]

        if start <= last_end:
           res[-1][1] = max(end, last_end)

        else:
            res.append([start, end])
    
    return res
               

n = [[1,3],[2,6],[8,10],[15,18]]
n1 = [[1,3]]
print(merge(n1))