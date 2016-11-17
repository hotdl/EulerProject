#coding:utf8

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

import math
import common

def next_prime(num):
    if num % 2 == 0 and num != 2:
        num += 1
    while not common.isPrime(num):
        num += 2
    return num

def large_primeFactor(num):
    i = 2
    while i < long(math.sqrt(num)/2):
        if num % i == 0:
            large = i
            # print large
        i = next_prime(i+1)
    return large

print large_primeFactor(600851475143)

