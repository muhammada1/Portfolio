#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    lst=list()
    if s.endswith('PM') is True:
        if s.startswith('12'):
            s=s.rstrip('PM')
            return(s)
        else:
            p=s.rstrip('PM')
            lst=p.split(':')
            lst[0] = int(lst[0])
            lst[0]=lst[0]+12
            lst[0] = str(lst[0])
            s=(lst[0]+':'+lst[1]+':'+lst[2] )
            return(s)
    else:
        s=s.rstrip('AM')
        if s.startswith('12'):
            s=s.replace('12', '00')
        return(s)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
