def two_pointer(nums, target):
    left , right = 0 , len(nums) -1

    while left < right :
        curr_sum = nums[left]+ nums[right]
        if curr_sum == target :
            return[left+1, right+1]
        elif curr_sum < target:
            left +=1
        else:
            right -= 1

nums = [2, 7, 11, 15]
target = 13 
print(two_pointer(nums, target))