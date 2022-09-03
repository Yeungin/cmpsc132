numList = [-8,-4,1,2,3,4,5,6]
def sumSquares(numList):
    x = 0
    for i in range(len(numList)):
        if (numList[i] > 5 and numList[i] < 500) or (numList[i]%4) == 0:
            square = numList[i] * numList[i]
            x += square 
    return x

print(sumSquares(numList))
