#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    hourglass = list()
    sums = list()
    n = 6 #  for a 6x6 matrix
    i, j = 0, 0
    for i in range(n-2):
        for j in range(n-2):
            for i in range(i, i+3):
                k=j
                for k in range(k, k+3):
                    hourglass.append(arr[i][k])
            del hourglass[3:6:2]
            j -= 2
            i -= 2
            sums.append(sum(hourglass))
            hourglass.clear() # or hourglass[:]

    print(max(sums))
