def squareroot(n):
    root = n/2                  #первоначальная догадка 1/2 от n
    for k in range(20):
        root = (1/2) * (root + (n / root))

    return root

if __name__ == '__main__':
    print(squareroot(9))
    print(squareroot(393924))
