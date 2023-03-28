def getMaxSubSum(a:list):
    maxS = 0
    for i in range(len(a)):
        sumFix = 0
        for j in range(i,len(a)):
            sumFix +=a[j]
            maxS = max(maxS,sumFix)
            j+=1
    return maxS
l = [1,2,3,4]
print(getMaxSubSum(l))