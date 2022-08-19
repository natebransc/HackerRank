# HackerRank Practice
# Given a square matrix, calculate the absolute difference between the sums of its diagonals.

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    n = len(arr[0])

    # primary diagonal
    primary = 0
    i = 0
    while i < n:
        primary += arr[i][i]
        i += 1

    # secondary diagonal
    secondary = 0
    i = n - 1
    j = 0
    while i >= 0:
        secondary += arr[i][j]
        i -= 1
        j += 1

    return abs(primary - secondary)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()