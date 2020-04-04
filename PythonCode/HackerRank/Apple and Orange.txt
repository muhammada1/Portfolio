#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    #between s and t
    #print(s,t,a,b,apples,oranges)
    count=0
    count2=0
    for splited in apples:
        x=a+splited
        if (x >= s) and (x <= t) is True:
            count +=1
        else:
            count +=0
    print(count)
    
    for tangerine in oranges:
        y=b+tangerine
        if (y >= s) and (y <= t) is True:
            count2 +=1
        else:
            count2 +=0
    print(count2)


if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
