# Using Precision Handling in Python

def plusMinus(array):
    # Write your code here
    total = len(array)
    positives = 0
    negatives = 0
    zeroes = 0
    
    for i in range(total):
        if array[i] > 0:
            positives +=1
        elif array[i] < 0:
            negatives += 1
        else:
            zeroes +=1
    
    r1 = positives/total
    r2 = negatives/total
    r3 = zeroes/total
    
    print("{0:.6f}".format(r1),"{0:.6f}".format(r2),"{0:.6f}".format(r3) )

plusMinus([1,0,0,0])