def foo(pattern, s):
    dictForPattern = {}
    dictForWord ={}
    splitString = s.split()   # default seperator is whitespace.
    for i, c in enumerate(pattern):
        if c not in dictForPattern:
            dictForPattern[c] = [i]
        
        else:
            dictForPattern[c].append(i)
        
    for i, c in enumerate(splitString):
        if c not in dictForWord: dictForWord[c] = [i]
        else: dictForWord[c].append(i)
    
    res = [x for x in dictForPattern.values()] == [x for x in dictForWord.values()] 
    return res


pattern = 'abba'
s = " dog cat cat dog"

res = foo(pattern, s)
print(res)