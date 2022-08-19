# HackerRank Practice Problem
# Given a list of integers, count and return the number of times each value appears as an array of integers.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    freq = []
    i = 0
    while i < 100:
        freq.append(0)
        i += 1

    for i in arr:
        freq[i] += 1

    return freq

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
