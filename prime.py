#!/usr/bin/env python3
import os 
import sys

def isPrime(n :int):
    j = 2
    factor = int(n//j)
    #for i in range(2,n//2+1):
    while factor > 1:
        j += 1
        if n%factor == 0: return False
        else: factor = int(n//j)
    return True

def primes(n :int):
    primeList = []
    j = 2
    factor = int(n//j)
    done = False
    counter = 0
    while factor > 1 and not done:
        j = 2
        counter += 1
        done = True
        #for i in range(factor,1,-1):
        while factor > 1:
            counter += 1
            j += 1
            if n%factor==0 and isPrime(factor):               
                primeList.insert(0,factor)               
                n /= factor
                if n>2: factor = int(n//2)
                else: factor=int(n)
                #done = False                                    
                break
            else:
                factor = int(n//j)

    if done: primeList.insert(0,int(n))
    print(counter)
    return primeList

# if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
#     n = int(sys.argv[1])
#     numbers = [3, 6, 10, 11,29,34]
#     for i in numbers:
#         print(f"{str(i)} is prime") if isPrime(i) else print(f"{str(i)} is not prime")
# else:
#     print("Enter a valid positive number ... ")

number = 600851475143
#print(primes(number))
print(isPrime(87625999))


