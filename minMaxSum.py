# HackerRank Practice Problem
# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def minMaxSum(arr):
    arr.sort()
    i = 0
    min = 0
    max = 0
    while i < 4:
        min += arr[i]
        i += 1
    i = -1
    while i > -5:
        max += arr[i]
        i -= 1

    print(str(min) + " " + str(max))


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    minMaxSum(arr)
