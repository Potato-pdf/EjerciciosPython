#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#
array = list(map(int, input().split()))

def reverseArray(a):
    # Write your code here
    return a[::-1]


if __name__ == '__main__':
    result = reverseArray(array)
    print(result)