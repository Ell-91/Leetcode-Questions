#Time: O(n log n) because we are sorting the array
#Space: O(n) may end up storing all the elements in the results array

def threeNumberSum(array, targetSum):
    array.sort() #sort in order
    triplets = []

    for i in range(len(array)-2):
        left_ptr = i + 1
        right_ptr = len(array) - 1

        while left_ptr < right_ptr:
            currentSum = array[i] + array[left_ptr] + array[right_ptr]

            if currentSum == targetSum:
                triplets.append([array[i], array[left_ptr], array[right_ptr]])
                right_ptr -= 1
                left_ptr += 1

            elif currentSum < targetSum:
                left_ptr += 1
            
            elif currentSum > targetSum:
                right_ptr -= 1
    return triplets

array = [-12, 3, 1, 2, -6, 5, -8, 6]
target = 0
print(threeNumberSum(array, target))