def twoSums(array, target):
    values = dict()

    for i in range(len(array)):
        complement = target - array[i]
        currentNum = array[i]
 
        if currentNum in values:
            return [values[currentNum], i]
        else:
            values[complement] = i


arr1 = [3, 5, 7, 8, 19]
target = 12 

print(twoSums(arr1, target))