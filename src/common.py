import math
import time
import functools

def is_prime(num):
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

def union_dict(dict1, dict2):
    for k, v in dict2.items():
        if k in dict1.keys():
            dict1[k] += v
        else:
            dict1[k] = v

def calc_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i*i != num:
                divisors.append(num/i)
    return divisors

def costtime(func):
    @functools.wraps(func)
    def ff(*args, **keys):
        st = time.time()
        res = func(*args, **keys)
        print "Cost time: %s" % (time.time()-st)
        return res
    return ff

