def arrayOfProducts(array):
    products = [1 for _ in range(len(array))] #Initialize an array of 1's

    leftRunningProduct = 1
    for i in range(len(array)):
        products[i] = leftRunningProduct
        leftRunningProduct *= array[i]
    
    rightRunningProduct = 1
    for i in reversed(range(len(array))):
        products[i] *= rightRunningProduct
        rightRunningProduct *= array[i]
    
    return products


 

array = [5, 1, 4, 2]
print(arrayOfProducts(array))