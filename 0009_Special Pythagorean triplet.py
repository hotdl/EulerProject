#coding:utf8

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
#
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def calc_pythagorean_triplet():
    for a in range(1,1000):
        for b in range(a+1, 1000-a+1):
            c = 1000 - a - b
            if a*a+b*b == c*c:
                return a, b, c

print reduce(lambda x,y:x*y, calc_pythagorean_triplet())

