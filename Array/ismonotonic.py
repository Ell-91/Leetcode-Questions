# Monotonic: Read from left to right, are all of these entirly non increaing or decreasing

# Time: O(n) because we iterate through the entire array
# Space: O(1) not storing any items
def ismonotonic(array):
    non_decreasing = True
    non_increasing = True 

    for i in range(1, len(array)):
        if array[i] < array[i - 1]:
            non_increasing = False
        if array[i] > array[i - 1]:
            non_decreasing = False
    return non_decreasing or non_decreasing



array = [-1, -5, -10, -1100, -1100, -1101, -1102, -9001]
print(ismonotonic(array))