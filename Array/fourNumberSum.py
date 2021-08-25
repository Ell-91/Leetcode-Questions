def fourNumberSum(array, targetSum):
    if array == [] or len(array) < 4:
        return False

    array.sort()
    result = []

    for i in range(len(array)-3):
        if i > 0 and array[i] == array[i-1]:
            continue
        for j in range(i + 1, len(array)-2):
            if j > i + 1 and array[j] == array[j-1]:
                continue

            left_ptr = j + 1
            right_ptr = len(array) - 1
            currentSum = array[i] + array[j] + array[left_ptr] + array[right_ptr]
           
            while left_ptr < right_ptr:
                if currentSum == targetSum:
                    result.append([array[i], array[j], array[left_ptr], array[right_ptr]])
                    left_ptr += 1
                    right_ptr -= 1

                    while left_ptr < right_ptr and array[left_ptr] == array[left_ptr - 1]:
                        left_ptr += 1

                    while left_ptr < right_ptr and array[right_ptr] == array[right_ptr + 1]:
                        right_ptr -= 1

                elif currentSum > targetSum:
                    right_ptr -= 1
                
                elif currentSum < targetSum:
                    left_ptr += 1
    return result
             


array = [7, 6, 4, -1, 1, 2] 
targetSum = 16
print(fourNumberSum(array, targetSum))