import math

def isPrime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if not num & 1:
        return False
    for x in range(3, int(math.sqrt(num))+1,2):
        if num % x == 0:
            return False
    return True