#coding:utf8

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, b
# egin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by
#  its alphabetical position in the list to obtain a name score.
#
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th
# name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
#
# What is the total of all the name scores in the file?

#file content format: "MARY","PATRICIA",..."ALONSO"
try:
    with open("../assets/p022_names.txt") as f:
        datas = sorted(map(lambda s: str.upper(s[1:-1]),f.read().split(",")))
        print sum([(i+1)*sum([(ord(x)-64) for x in datas[i]]) for i in range(len(datas))])

except IOError:
    print "Make sure the file exists."

