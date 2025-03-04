def func(nums):
    for i in nums:
        if i == 1:
            nums.remove(1)
            nums.append(1)
    for i in nums:
        if i == 2:
            nums.remove(2)
            nums.append(2)


nums = [2,0,2,1,1,0]
func(nums)
print(nums)