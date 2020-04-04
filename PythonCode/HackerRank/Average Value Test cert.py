#!/bin/python3

import math
import os
import random
import re
import sys


def avg(*nums):
    #numerator
    answernum=sum(nums)
    #denominator
    c=len(nums)
    
    #numerator/denominator
    total=answernum/c
    #Adds second decimal
    total= format(total, '.2f')
    total=float(total)
    return(total)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    nums = list(map(int, input().split()))

    res = avg(*nums)
    
    fptr.write('%.2f' % res + '\n')

    fptr.close()

    print(res)
