#coding:utf8

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
#
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
#
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

from common import costtime

def recursive_calc_ways(money, coins, index = 0):
    coin = coins[index]
    if coin == 1:
        return 1
    else:
        ways = 0
        for i in range(money//coin+1):
            ways += recursive_calc_ways(money-i*coin, coins, index+1)
        return ways

@costtime
def calc_ways(money, coins, index = 0):
    return recursive_calc_ways(money, coins, index)

print calc_ways(money = 200, coins = (200, 100, 50, 20, 10, 5, 2, 1))

