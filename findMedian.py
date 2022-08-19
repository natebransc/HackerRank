def findMedian(arr):
    arr.sort()
    size = len(arr)
    middle = int(((size + 1)/2) - 1)

    return arr[middle]

print(str(findMedian([1, 8, 34, 3, 6])))