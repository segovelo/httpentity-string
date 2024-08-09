#!/usr/bin/env python3
import os 
import sys

def isPrime(n :int):
    for i in range(2,n//2+1):
        if n%i == 0: return False
    return True

def primes(n :int):
    primeList = []
    prime = n//2
    done = False
    counter = 0
    while prime > 1 and not done:
        counter += 1
        done = True
        for i in range(prime,1,-1):
            counter += 1
            if n%i==0 and isPrime(i):               
                primeList.insert(0,i)
                n /= i
                if n>2: prime = int(n//2)
                else: prime=int(n)
                done = False                                    
                break        
    print(counter)
    return primeList

# if len(sys.argv) > 1 and int(sys.argv[1]) > 0:
#     n = int(sys.argv[1])
#     numbers = [3, 6, 10, 11,29,34]
#     for i in numbers:
#         print(f"{str(i)} is prime") if isPrime(i) else print(f"{str(i)} is not prime")
# else:
#     print("Enter a valid positive number ... ")

number = 1300
print(primes(number))

