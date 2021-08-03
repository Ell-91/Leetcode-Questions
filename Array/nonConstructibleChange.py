# O(nlogn) + n (+n because we have to iterate through the array) because we have to sort our input array and then loop through array one time
# fastest we can sort our array is nlogn (mergesort or quicksort)
# O(1) because we sort array in place, use the existing array that is given to us

#Ask if we can sort the input array in place, 
#If we cant sort in place its O(n) because you need to create a new data structure to 
# store the sorted array
def nonConstructibleChange(coins):
    coins.sort() #sort array in place
    
    currentChangeCreated = 0
    
    #loop through all the coins
    for i in range(len(coins)):
        if coins[i] > currentChangeCreated + 1:
            return currentChangeCreated + 1

        currentChangeCreated += coins[i]
        
    return currentChangeCreated + 1
	

    

coins = [5, 7, 1, 1, 2, 3, 22]

print(nonConstructibleChange(coins))