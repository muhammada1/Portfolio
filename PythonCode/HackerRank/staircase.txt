#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the staircase function below.
def staircase(n):
    o=1

    while o<=n:
        y=('#'*o)
        x=(' '*(n-o))
        print(x+y)
        o = o +1

        

if __name__ == '__main__':
    n = int(input())

    staircase(n)
