def smallestDifference(arrayOne, arrayTwo):
	# O(n logn) to sort arrayOne O(m logm) to sort arrayTwo
	#O(n logn + m logm)
	#Space O(1) because we're sorting arrays in place and not
	# not storing any aditional memory, just keeping track of our
	#best pair
	arrayOne.sort()
	arrayTwo.sort()
	
	# Indicies our pointers are pointing to 
	indx_one = 0
	indx_two = 0
	
	smallestDifference = float("inf")
	currentDifference = float("inf")
	
	smallestPair = []
	
	while indx_one < len(arrayOne) and indx_two < len(arrayTwo):
		first_num = arrayOne[indx_one]
		second_num = arrayTwo[indx_two]
		
		#currentDifference = abs(first_num - second_num)
		
		if first_num == second_num:
			return [first_num, second_num]
		
		elif first_num < second_num:
			currentDifference = second_num - first_num
			indx_one += 1
		
		elif second_num < first_num:
			currentDifference = first_num - second_num
			indx_two += 1
			
    #check if smallest difference needs to be updated
		if smallestDifference > currentDifference:
			smallestDifference = currentDifference
			
			smallestPair = [first_num, second_num]
			
	return smallestPair

arr1 = [-1, 5, 10, 20, 28,3]
arr2 = [26, 134, 135, 15, 17]

print(smallestDifference(arr1, arr2))