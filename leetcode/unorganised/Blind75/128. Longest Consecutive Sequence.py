def longestConsecutive(nums):
    numSet = set(nums)
    longest = 0
    for num in nums:
        if (num -1) not in nums:
            length = 1
            while (num + length) in numSet:
                length += 1
            longest = max(longest, length)
    return longest

nums = [100,4,200,1,3,2]
print(longestConsecutive(nums))