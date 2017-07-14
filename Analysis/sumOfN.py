def sumOfN(n):
    theSum = 0
    for i in range(1, n+1):
        theSum += i
    
    return theSum

if __name__ == '__main__':
    print(sumOfN(10))