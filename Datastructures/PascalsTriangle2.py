def func(rowIndex):
    res = [1]

    for i in range(rowIndex):
        temp = [0] + res + [0]
        o = []
        for j in range(len(temp)-1):
            o.append(temp[j] + temp[j+1])

        res = o
    return res 

print(func(5))