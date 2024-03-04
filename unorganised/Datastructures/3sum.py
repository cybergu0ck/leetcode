def func(num):
    num.sort()
    res = []
    #o= []
    for i, a in enumerate(num):
        if (i >0 and a == num[i -1]):
            continue
        l = i +1 
        r = len(num)-1
        while (l < r):
            sum = num[i] + num[l] + num[r]
            if (sum > 0):
                r -= 1
            elif (sum < 0):
                l += 1
            else:
                res.append([num[i], num[l], num[r]])
                l +=1
                while (num[l] == num[l-1] and l < r):
                    l+=1
    return res


nums = [0,0,0,0]
print(func(nums))