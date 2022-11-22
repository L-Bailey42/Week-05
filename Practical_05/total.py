#!/usr/bin/env python3

import sys


if __name__ == "__main__":
    count = len(sys.argv)
    total = 0
    while count > 1:
        count -= 1
        total += float(sys.argv[count])
    avg = total/len(sys.argv)

    print("Total is", total)
    print("Average is", avg) 

