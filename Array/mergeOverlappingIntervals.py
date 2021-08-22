def mergeOverlappingIntervals(intervals):
    #check if the list is empty

    #sort the intervals
    intervals.sort()

    #Initialize a variable to hold the merged intervals
    merged_intervals = []
    #print(merged_intervals[-1][1])

    #start times are indexed at 0 // end times are indexed at 1
    
    for interval in intervals:
        if merged_intervals == [] or merged_intervals[-1][1] < interval[0]:
            merged_intervals.append(interval) #add interval to results
            
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])    
    return print(merged_intervals)
    #print(intervals[0])


interval = [[1,3],[2,6],[15,18],[8,10]]
mergeOverlappingIntervals(interval)