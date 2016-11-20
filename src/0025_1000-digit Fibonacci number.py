#coding:utf8

# The Fibonacci sequence is defined by the recurrence relation:
#
# Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
# Hence the first 12 terms will be:
#
# F1 = 1
# F2 = 1
# F3 = 2
# F4 = 3
# F5 = 5
# F6 = 8
# F7 = 13
# F8 = 21
# F9 = 34
# F10 = 55
# F11 = 89
# F12 = 144
# The 12th term, F12, is the first term to contain three digits.
#
# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?


# mySolve
# class BigNum():
#     def __init__(self, strNum):
#         self.__parse_str_2_list(strNum)
#
#     def __parse_str_2_list(self, strNum):
#         self.__data = []
#         for i in range(len(strNum)):
#             self.__data.append(strNum[i])
#
#     def __str__(self):
#         strNum = ""
#         for c in self.__data:
#             strNum += str(c)
#         return strNum
#
#     def __repr__(self):
#         return self.__str__()
#
#     def __add__(self, other):
#         data1 = copy.copy(self.__data)
#         data2 = copy.copy(other.__data)
#         data1.reverse()
#         data2.reverse()
#         length = max(len(data1), len(data2))
#         data = []
#         up = 0
#         for i in range(length):
#             num = self.__getNum(data1, i) + self.__getNum(data2, i) + up
#             if num >= 10:
#                 up = 1
#                 num -= 10
#             else:
#                 up = 0
#             data.append(num)
#         if up == 1:
#             data.append(1)
#         data.reverse()
#         return BigNum(data)
#
#     def __len__(self):
#         return len(self.__data)
#
#     def __getitem__(self, item):
#         return self.__data[item]
#
#     def __getNum(self, data, index):
#         if index < len(data):
#             return int(data[index])
#         else:
#             return 0
# bn1 = BigNum("1")
# bn2 = BigNum("1")
# count = 1
# while len(bn2) < 1000:
#     bn1, bn2 = bn2, bn1+bn2
#     count += 1
# print count+1


# webSolve
# F(n+1) = F(n-1) + F(n)
# F(n+1) = F(n-1) + F(n)
# F(n-1) <= p^(n-2)
# F(n) <= p^(n-1)
# F(n+1) <= p^(n-2) + p^(n-1)
# F(n + 1) <= (p ^ (n - 2))(1 + p)
# F(n+1) <= p^n
# 1 + p = p^2
# p = (1 + sqrt(5))/2
# k <= p^(n-1)
# log(k) <= (n-1)(log(p))
# n <= log(k)/log(p) + 1
# println(math.ceil(999/math.log10((1 + math.sqrt(5))/2) + 1).toInt)
import math

print int(math.ceil(999/math.log10((1+math.sqrt(5))/2)+1))

