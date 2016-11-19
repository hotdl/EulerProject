#coding:utf8

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

import common

def calc_sum_proper_divisors(num):
    return sum(common.calc_divisors(num))-num

num = 10000
arr = [calc_sum_proper_divisors(x) for x in range(num)]
total = 0
for i in range(2, num):
    if arr[i] < num and arr[arr[i]] == i and i != arr[i]:
        total += i
print total


