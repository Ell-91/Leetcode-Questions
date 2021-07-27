def threeSum(nums):
    result = [] 
    nums.sort()  

    for count, value in enumerate(nums):
        print(count, value)
        if count > 0 and value == nums[count]:
            continue 

        left_ptr, right_ptr = count + 1, len(nums) - 1
        while left_ptr < right_ptr:
            threeSum = value + nums[left_ptr] + nums[right_ptr]:
            if threeSum > 0:
                right_ptr -= 1
            elif threeSum < 0:
                left_ptr += 1
            else:
                result.append(a, nums[left_ptr], nums[right_ptr])
                left_ptr += 1
                while nums[left_ptr] == nums[left_ptr - 1] and left_ptr < right_ptr:
                    left_ptr _+= 1








num1 = [-1,0,1,2,-1,-4]
num2 = [0]
num3 = []

print(threeSum(num1))
print(threeSum(num2))
print(threeSum(num3))
