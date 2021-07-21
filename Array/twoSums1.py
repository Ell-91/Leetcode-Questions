# Time complexity O(n^2)       Space Complexity O(n)
def twoSums(array, target):
    for i in range(len(array)):
        for j in range(i+1, len(array)):
            if array[i] + array[j] == target:
                return [i,j]
 



arr1 = [3, 5, 6, 8, 19]
target = 22

print(twoSums(arr1, target))