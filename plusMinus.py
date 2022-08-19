# HackerRank Practice Problem
# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of each fraction on a new line with  places after the decimal.


#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    size = len(arr)
    pos = 0
    neg = 0
    zero = 0


    for i in arr:
        if i > 0:
            pos += 1
        elif i == 0:
            zero += 1
        else:
            neg += 1

    print(round(pos/size, 6))
    print(round(neg / size, 6))
    print(round(zero / size, 6))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
