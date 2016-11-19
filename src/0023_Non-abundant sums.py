#coding:utf8

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the
# sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
# abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as
# the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known
# that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

import common

all_abundant_numbers = [x for x in range(12,28123-10) if sum(common.calc_divisors(x))-x-x>0]

all_sum = 28124*28123/2
abundant_num_sum_set = set([])
length = len(all_abundant_numbers)
for i in range(length):
    for j in range(i, length):
        res = all_abundant_numbers[i] + all_abundant_numbers[j]
        if res <= 28123:
            abundant_num_sum_set.add(res)

print all_sum-sum(abundant_num_sum_set)

