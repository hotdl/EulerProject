#coding:utf8

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?

import common

def next_prime(num):
    if num % 2 == 0 and num != 2:
        num += 1
    while not common.is_prime(num):
        num += 2
    return num

i = 0
prime = 0
while i < 10000:
    prime = next_prime(prime+1)
    i += 1
print prime
