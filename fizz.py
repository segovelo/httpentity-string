#!/usr/bin/env python3
import os 
import sys

def fizzbuzz(n):
    if n == 0: return
    fizzbuzz(n-1)
    if n%15 == 0:
        print("fizz-buzz")
    elif n%5 == 0:
        print("buzz")
    elif n%3 == 0:
        print("fizz")
    else:
        print(n)
    return

if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
    n = int(sys.argv[1])
    fizzbuzz(n)
else:
    print("Enter a valid positive number ... ")