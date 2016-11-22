#coding:utf8

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: as 1! = 1 and 2! = 2 are not sums they are not included.

from common import costtime

@costtime
def main():
    fact = lambda x: reduce(lambda x, y: x*y, range(1, x+1), 1)
    fact_list = [fact(x) for x in range(0,10)]

    def fact_sum(num):#4.5s
        res = 0
        while num > 0:
            res += fact_list[num%10]
            num /= 10
        return res
    # fact_sum = lambda x: sum([fact_list[int(i)] for i in str(x)]) #13s

    n = 1
    while True:
        if n*fact_list[9] < 10**n:
            break
        n += 1

    result = 0
    for i in range(10, n*fact_list[9]):
        if fact_sum(i) == i:
            result += i

    print result

main()

