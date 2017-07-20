def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionOfMax = 0

        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]

if __name__ == '__main__':
    alist = [52, 25, 93, 34, 55, 124, 55, 44, 123, 32]
    selectionSort(alist)
    print(alist)