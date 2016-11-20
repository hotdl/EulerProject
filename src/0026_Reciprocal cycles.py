#coding:utf8

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:
#
# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
#
# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

def calc_value_has_longest_cycle(limit):
    max_len = 0
    num = 0
    for n in range(limit,1,-1):
        mods = []
        mod = 1
        cycle_len = 0
        count = 0
        while mod > 0:
            count += 1
            mods.append(mod)
            mod *= 10
            x = mod / n
            mod = mod % n
            if mod in mods:
                cycle_len = count - mods.index(mod)
                break
        if cycle_len > max_len:
            max_len = cycle_len
        if max_len > n-2:
            num = n
            break
    return num

print calc_value_has_longest_cycle(999)

