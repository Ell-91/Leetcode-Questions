def subarraySort(array):
    # Error checking 
    if array == [] or len(array) < 2:
        return 0
    
    n = len(array)
    currentMax = array[0]
    r = 0

    for i in range(1, len(array)):
        if array[i] < currentMax:
            r = i
        else:
            currentMax = array[i]
    
    currentMin = array[-1]
    l = 0
    for i in range(n-2, -1, -1):
        if array[i] > currentMin:
            l = i
    return r - l + 1 if l != r else 0

    
array = [2, 6, 4, 8, 10, 9, 15]   #[6,4,8,10,9]  need to be sorted, has length 5
print(subarraySort(array))