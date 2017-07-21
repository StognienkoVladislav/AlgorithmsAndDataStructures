def mergeSort(alist):
    print("Splitting", alist)

    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf  = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0

        while i < len(lefthalf) and j <len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1

            else:
                alist[k] = righthalf[j]
                j += 1

            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

    print("Merging", alist)

if __name__ == '__main__':
    alist = [54, 26, 93, 18, 88, 44, 55, 23]
    mergeSort(alist)
    print(alist)