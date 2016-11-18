#coding: utf8

# You are given the following information, but you may prefer to do some research for yourself.
#
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

is_leap_year = lambda year: (year%400 == 0) or (year%4 == 0 and year % 100 != 0)
calc_next_year_month = lambda year, month: (month == 12) and (year+1,1) or (year, month+1)
calc_month_days = lambda year, month: (month==2 or month in (4, 6, 9, 11)) and (month == 2 and (is_leap_year(year) and 29 or 28) or 30) or 31
is_sunday = lambda d: d==0

def generate_days(year, month, day, eYear, eMonth):
    while not (year == eYear and month == eMonth):
        yield day
        day = (day + calc_month_days(year, month)%7)%7
        year, month = calc_next_year_month(year, month)

first_day_1900_01 = [d for d in generate_days(1900, 1, 1, 1901, 2)][-1]
print len(filter(is_sunday,([d for d in generate_days(1901, 1, first_day_1900_01, 2001, 1)])))

