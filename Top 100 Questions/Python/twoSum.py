class Solution:
  #Brute Force O(n^2) runtime    O(n) space 
  '''def BruteForceTwoSums(self,nums, target):
    for i in range(len(nums)):
      for j in range(j+1, len(nums)):
        sum = nums[i] + nums[j]
        if sum == target:
          return [i,j]
        else:
          return print("target not found")'''
          
  #Optimal solution O(n) runtime O(n) space complexity 
  def OptimalTwoSums(self, nums, target):
    hashMap = dict() #linear probing

    for i in range(len(nums)):
      num = nums[i]
      complement = target - num #complement is 7
      
      if num in hashMap:
        return [hashMap[num], i] #{7:0} 7 stores at index 0, its the first complement
      else:
        hashMap[complement] = i

sol = Solution()
num1 = [2,5,6,7]
target1 = 7

num2 = [2,5,6,7]
target2 = 9

print(sol.OptimalTwoSums(num1, target1))


