#!/usr/bin/env python3
import os 
import sys


def isPalindrome(string):
    string = string.lower()
    if len(string) <= 2: return string[0] == string[-1]
    if string[0] != string[-1]: return False
    return isPalindrome(string[1:-1])


if len(sys.argv) > 1:
    string = sys.argv[1]
    print(isPalindrome(string))
else:
    print("Enter a valid argument ... ")