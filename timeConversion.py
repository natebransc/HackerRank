# HackerRank Practice Problem
# Given a time in -hour AM/PM format, convert it to military (24-hour) time.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ampm = s[-2]
    hour = int(s[:2])
    if ampm == "A" and hour == 12:
        hour = 0
    elif ampm == "P" and hour != 12:
        hour += 12


    hourstr = str(hour)
    if len(hourstr) == 1:
        hourstr = "0" + hourstr
    military = s.replace(s[:2], hourstr, 1)

    return military[:8]


print(timeConversion("12:00:00PM"))