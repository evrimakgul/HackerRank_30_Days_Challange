#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    binary = f'{n:b}'

    consecutive = 0
    highest = 0
    for i in binary:
        if i == '1':
            consecutive += 1
            if highest < consecutive:
                highest = consecutive
        else:
            consecutive = 0

    print(highest)
