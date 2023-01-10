def foo(s):
    dict = {}
    res =0
    oddFlag = False
    for i in s:
        if i in dict.keys():
            dict[i] +=1
        else:
            dict[i] =1
    
    for i in dict.values():
        if (i % 2 == 0):
            res +=i
        else:
            oddFlag = True
            res += (i-1)
    if oddFlag:
        res += 1
        
    return res

ip = "abccccdd"
res = foo(ip)
print(res)