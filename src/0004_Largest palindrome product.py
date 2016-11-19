#coding:utf8

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
import time
def is_palindromic(num):
    numStr = str(num)
    for i in range(len(numStr)):
        if numStr[i] != numStr[-1-i]:
            return False
    return True

def calc_palindrome(num):
    large = 0
    for i in range(num, 0, -1):
        for j in range(i, 0, -1):
            res = i * j
            if is_palindromic(res) and res > large:
                large = res
    return large

print calc_palindrome(999)


