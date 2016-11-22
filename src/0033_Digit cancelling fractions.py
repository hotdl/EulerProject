#coding:utf8

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly
# believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits
# in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

import common

def simplify(x, y):
    for cx in str(x):
        for cy in str(y):
            if cx != "0" and cx == cy:
                return int(str(x).replace(cx, "", 1)), int(str(y).replace(cy, "", 1))
    return x, y

def find_simplify_targets():
    simplify_targets = []

    for i in range(10, 100):
        for j in range(i+1, 100):
            x, y = simplify(i, j)
            if x != i and x * j == y * i:
                simplify_targets.append((x, y))

    return simplify_targets

def reduce_multi(list):
    return reduce(lambda x, y: int(x)*int(y), list)

@common.costtime
def main():
    targets = find_simplify_targets()
    numerator = reduce_multi([x[0] for x in targets])
    denominator = reduce_multi([x[1] for x in targets])
    print denominator/common.gcd(numerator, denominator)

main()

