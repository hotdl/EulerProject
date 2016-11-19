#coding:utf8

# A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3
# and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic
# permutations of 0, 1 and 2 are:
#
# 012   021   102   120   201   210
#
# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?


# fact = lambda i:reduce(lambda x,y:x*y, range(1,i+1),1)

def lexicographic_perm(num, list):
    length = len(list)

    fact_list = [1]
    for i in range(1, length):
        fact_list.append(i*fact_list[i-1])

    res_list = []
    for i in range(length,0,-1):
        x = (num-1) / fact_list[i-1]
        mod = (num-1) % fact_list[i-1]
        res_list.append(list[x])
        list.remove(list[x])
        num -= x*fact_list[i-1]
    return reduce(lambda x,y:str(x)+str(y), res_list)

print lexicographic_perm(1000000,range(10))

