#coding:utf8

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

import array

def collatz(num):
    if num == 1:
        return 1
    if num & 1:
        num = 3 * num + 1
    else:
        num = num >> 1
    return num

def calc_collatz_sequence_length(num):
    data = {}
    data[1] = 1
    for i in range(2, num):
        num = i
        length = 0
        while num > 1:
            num = collatz(num)
            length += 1
            if data.has_key(num):
                data[i] = length + data[num]
                break
    return data

max = 0
num = 0
dict = calc_collatz_sequence_length(1000000)
for x in dict.keys():
    if dict[x] > max:
        max = dict[x]
        num = x
print num


