#coding:utf8
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import common

def add_count(dict, num, count = 1):
    if(dict.has_key(num)):
        dict[num] += count
    else:
        dict[num] = count

def update_count(dict, num, count):
    dict[num] = count

def join_dict(dict1, dict2):
    dict = {}
    for k in dict1.keys():
        update_count(dict, k, dict1.get(k))
    for k in dict2.keys():
        if dict.has_key(k):
            if dict2.get(k) > dict.get(k):
                update_count(dict, k, dict2.get(k))
        else:
            update_count(dict, k, dict2.get(k))
    return dict

def calc_prime_factor(num, dict):
    for i in range(2, num+1):
        if num % i == 0 and common.is_prime(i):
            add_count(dict, i)
            calc_prime_factor(num/i, dict)
            break

def join_total_dict(num):
    joinDict = {}
    for i in range(1, num+1):
        dict = {}
        calc_prime_factor(i, dict)
        joinDict = join_dict(joinDict, dict)
    return joinDict

num = 1
joinDict = join_total_dict(20)
for k in joinDict.keys():
    num *= pow(k, joinDict.get(k))
print num

