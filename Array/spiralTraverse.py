def spiralTraverse(array):
    spiralOrder = []
    #for x, y in enumerate(array):
        #if x == len(y) - 1:
        #spiralOrder.append(y)

    for i in range(len(array)):
        spiralOrder.append(array[i])

    return spiralOrder

array =[[1,2,3,5], [12, 13, 14,5], [11, 16, 15, 6], [10, 9, 8,7]]
print(spiralTraverse(array))