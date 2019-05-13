"""
设a、b、c 均是0 到9 之间的数字，
abc、bcc 是两个三位数，且有：abc+bcc=532。
求满足条件的所有a、b、c 的值。
"""

# 自己写的
# sum部分可以直接用算式算，比强类型转换的内存使用少一些
for a in range(1, 6):
    for b in range(1, (6 - a)):
        for c in range(10):
            sum = int(str(a) + str(b) + str(c)) + int(str(b) + str(c) + str(c))
            if sum == 532:
                print("{0} {1} {2}".format(a, b, c))
