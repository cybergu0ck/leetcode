def func(nums, target):
    hashMap = {}
    for i in range(0, len(nums)):
        calc = target - nums[i]
        if (calc in hashMap):
            return [i, hashMap[calc]]
        else:
            hashMap[nums[i]] = i




print(func([3,2,4],6))

'''
def func(nums, target):
    o = []
    for i in range(0, len(nums)-1):
        for j in range(i+1,len(nums)):
            if((nums[i] + nums[j]) == target):
                o.append(i)
                o.append(j)
    return o
                
print(func([2,5,10,14],15))

'''
