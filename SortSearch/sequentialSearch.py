def sequentialSearch(alist, item):
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1

    return found

def orderedSequentialSearch(alist, item):
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:

        if alist[pos] == item:
            found = True

        else:

            if alist[pos] > item:
                stop = True

            else:
                pos = pos + 1

    return found


if __name__ == '__main__':
    testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
    print(sequentialSearch(testlist, 3))
    print(sequentialSearch(testlist, 19))

    testlist2 = [0, 1, 2, 8, 13, 17, 19, 32, 42]
    print(orderedSequentialSearch(testlist2, 3))
    print(orderedSequentialSearch(testlist2, 13))