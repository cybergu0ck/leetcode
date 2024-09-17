def search(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = int((low + high) / 2)
        if nums[mid] == target:
            return mid

        elif nums[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    else:
        return None


nums = [1, 2, 3, 4, 5, 6]
target = 7
print(search(nums, target))
