def majorityElement(nums):
        hashtable = dict()
        max = 0
        
        for i in nums:
            if (i not in hashtable):
                hashtable[i] = 0
            else:
                hashtable[i] += 1
            
        for i in hashtable.values():
            if(i > max):
                max = i
        
        value = (i for i in hashtable if hashtable[i]==max)
        return value

print(majorityElement([1,1,12,12,12,12]))