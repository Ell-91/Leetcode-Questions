def firstDuplicateValue(array):
    array.sort()
    for i in range(len(array)):
        if array[i] == array[i + 1]:
            return array[i]
    return []

array = [2, 1, 5, 2, 3, 3, 4]
print(firstDuplicateValue(array))
