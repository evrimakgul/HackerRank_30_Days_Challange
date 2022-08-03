#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    string = str(arr.pop())
    for i in range(n-1):
        string = string + " " + str(arr.pop())
    print(string)
