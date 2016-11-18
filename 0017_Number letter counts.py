#coding utf8

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen)
#
# contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

import common

#one,two,three,four,five,six,seven,eight,nine,ten,eleven,twelve,thirteen,fourteen,fifteen,sixteen,seventeen,eighteen,nineteen
ONE_2_NINETEEN_LIST = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
#twenty,thirty,forty,fifty,sixty,seventy,eighty,ninety
TWENTY_2_NINETY_LIST = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

def calc_letter_num(n):
    if n < 20:
        return ONE_2_NINETEEN_LIST[n]
    elif n < 100:#twenty,twenty-one...
        return TWENTY_2_NINETY_LIST[n/10] + ONE_2_NINETEEN_LIST[n%10]
    elif n < 1000:#one hundred, one hundred and one,...,one hundred and tweenty-one,...
        mod = n % 100
        if mod == 0:#[one] hundred
            return ONE_2_NINETEEN_LIST[n/100] + 7
        else:#[one] hundred and [one]
            return ONE_2_NINETEEN_LIST[n/100] + 7 + 3 + calc_letter_num(mod)
    elif n == 1000:#one thousand
        return 11
    else:#not implemented
        return 0

total = 0
for i in range(1, 1001):
    total += calc_letter_num(i)
print total

