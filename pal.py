#!/usr/bin/env python3
import os 
import sys


def isPalindrome(string):
    if len(string) < 2: return True
    if string[0].lower() != string[-1].lower(): return False
    return isPalindrome(string[1:-1])


if len(sys.argv) > 1:
    string = sys.argv[1]
    print(isPalindrome(string))
else:
    print("Enter a valid argument ... ")
