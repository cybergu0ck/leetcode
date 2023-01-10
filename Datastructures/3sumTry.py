
def func(num):
    num.sort()
    res =[]
    o = [] 
    for i in range(0, len(num)-2):
        l = i+1
        r = len(num)-1

        while(l < r):
            sum = num[i] + num[l] + num[r]
            if(sum > 0):
                r -= 1
            elif (sum < 0):
                l += 1
            else:
                o.append([num[i],num[l],num[r]])
                o.sort()
                res.append(o[:])
                o.pop()
                o.pop()
                o.pop()

        
        for i in range(0,len(res)-1):
            for j in range(i+1, len(res)):
                if res[i] == res[j]:
                    del res[j]

    return res

print(func([-2,0,1,1,2]))



""" def func(nums):
    hashMap = {}
    res = []
    o = []
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            calc = 0 - nums[i] - nums[j]
            if(calc in nums):
                if(((i != j) & (i != nums.index(calc)) & (j != nums.index(calc)))):
                    if(calc in hashMap):
                        o.append(nums[i])
                        o.append(nums[j])
                        o.append(calc)
                        o.sort()
                        res.append(o[:])
                        o.pop()
                        o.pop()
                        o.pop()

                    for i in range(0, len(res)-1):
                        for j in range(i+1, len(res)):
                            if res[i] == res[j]:
                                del(res[j])                   
                    else:
                        hashMap[nums[i]] = i
                        hashMap[nums[j]] = j
            else:
                hashMap[nums[i]] = i
                hashMap[nums[j]] = j
    count = 0
    for i in nums:
        if nums[i] == 0:
            count += 1 
    if(count == len(nums)):
        return [0,0,0]
    else:        
        return res

i = [-1,0,1,2,-1,-4]
i1 = [-1,0,1,2,-1,-4,-2,-3,3,0,4]
i2= [-1,0,1]
print(func(i1)) """







"""
def func(nums):
    res = []
    o = []
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)-1):
                if (((i != j) & (i != k) & (j != k)) & (nums[i] + nums[j] + nums[k] == 0 )):
                    o.append(nums[i])
                    o.append(nums[j])
                    o.append(nums[k])
                    o.sort()
                    #print(o)
                    if (len(o) == 3):
                        res.append(o[:])
                        o.pop()
                        o.pop()
                        o.pop()
                        #print(o)
                    for i in range(0, len(res)-1):
                        for j in range(i+1, len(res)):
                            if res[i] == res[j]:
                                del(res[j])
    
    if (res == []):
        return [0,0,0]
    else:                
        return res

i = [-1,0,1,2,-1,-4]
print(func(i))
print(len(i))

"""
Bhaigan


#[34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]


Bhaigan
