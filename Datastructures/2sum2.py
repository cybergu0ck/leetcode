def twoSum(numbers, target):
        l = 0
        r = len(numbers)-1
        while(numbers[l] + numbers[r] != target):
            if (numbers[l] + numbers[r] > target):
                r -= 1
            elif(numbers[l] + numbers[r] < target):
                l += 1
        return [l+1,r+1]

nums = [2,7,11,15]
target = 9
print(twoSum(nums, target))