def twoSums(array, target):
    values = dict()

    for i in range(len(array)): 
        complement = target - array[i]
        if complement in values:
            return [array[i], complement[i]]
        else:
            values[i] = complement[i]


arr1 = [3, 5, 7, 8, 19]
target = 12 

twoSums(arr1, target)