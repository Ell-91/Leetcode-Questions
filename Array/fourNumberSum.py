def fourNumberSum(array, targetSum):
    array.sort()
    quadruplets = dict()
    results = []

    for i in range(len(array)):
        for j in range(len(array)):
            currentSum = array[i] + array[j]
            complement = targetSum - currentSum

            quadruplets[currentSum] = i
    return quadruplets


array = [7, 6, 4, -1, 1, 2] 
targetSum = 16
print(fourNumberSum(array, targetSum))