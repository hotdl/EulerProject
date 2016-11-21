#coding:utf8

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
#
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
#
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
#
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

from common import costtime

def is_pandigital(x, y):
    if "0" in str(x) or "0" in str(y):
        return False
    r = x * y
    if "0" in str(r):
        return False
    li = str(x)[0:] + str(y)[0:] + str(r)[0:]
    return len(set(li)) == 9 and len(li) == 9

@costtime
def calc_all_pandigital():
    tps = []
    for x in range(2, 10):
        for y in range(1001, 10000):
            if is_pandigital(x, y):
                tps.append((x, y, x * y))
    for x in range(11, 100):
        for y in range(101, 1000):
            if is_pandigital(x, y):
                tps.append((x, y, x * y))
    return tps

print sum(set([x[2] for x in calc_all_pandigital()]))

