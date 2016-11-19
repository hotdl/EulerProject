#coding:utf8

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

import common

def next_prime(num):
    if num % 2 == 0 and num != 2:
        num += 1
    while not common.isPrime(num):
        num += 2
    return num

summary = 0
prime = 0
while prime < 2000000:
    prime = next_prime(prime+1)
    summary += prime
print summary-prime+2

