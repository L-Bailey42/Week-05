#!/usr/bin/env python3

import sys

def average(values):
    """ Calculates the average of the given list. """
    total = 0;
    for n in values: 
        total += float(n)   	 
    return total/len(values)


if __name__ == "__main__":
    print("Welcome, utils module has been imported and initialised!")
    if len(sys.argv) > 1:
        print("Average is ", average(sys.argv[1:]))