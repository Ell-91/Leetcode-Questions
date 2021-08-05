def moveElementToEnd(array, toMove):
    i = 0
    j = len(array) - 1
    
    while i < j:
        while array[j] == toMove:
            j -= 1
        if array[i] == toMove:
            array[i], array[j] = array[j], array[i]
        i += 1
    return array

array = [1, 1, 2, 2, 2, 3, 4, 4]
move = 2
print(moveElementToEnd(array, move))


'''#This would be O(n logn) time 
def moveElementToEnd(array, toMove):
    array.sort()
    
    for i in range(len(array)):
        toSwap = array[i]
        endOfArray = array[len(array) - 1]

        if toSwap == toMove:
            toSwap, endOfArray = endOfArray, toSwap
            print(array)
    return array'''

