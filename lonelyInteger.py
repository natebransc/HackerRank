# HackerRank Practice
# Given an array of integers, where all elements but one occur twice, find the unique element.

def lonelyinteger(a):
    a.sort()
    i = 0

    while i < (len(a) - 1):
        curr = a[i]
        next = a[i + 1]

        if curr != next:
            return curr
        
        i += 2

    return a[i]

print(lonelyinteger([1, 2, 3, 2, 1, 4, 4, 5, 5]))