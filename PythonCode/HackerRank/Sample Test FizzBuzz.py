#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'fizzBuzz' function below.
#
# The function accepts INTEGER n as parameter.
#

def fizzBuzz(n):
    for i in range(n):
        i=i+1
        if 0==(i % 3) and 0==(i % 5):
            print('FizzBuzz')
        elif 0==i%3:
            print('Fizz')
        elif 0==i%5:
            print('Buzz')
        else:
            print(i)

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
