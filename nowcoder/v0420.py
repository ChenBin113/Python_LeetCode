"""
一个小球，从高为H的地方下落，下落弹地之后弹起高度为下落时的一半，
比如第一次弹起高度为H/2，如此往复，
计算从小球H 高度下落到第n 次弹地往返的总路程。
"""
m = int(input())
for i in range(m):
    H, n = input().split()
    H = int(H)
    n = int(n)

    if n == 1:
        h1 = H
        print("{:.2f}".format(h1))
    elif n == 2:
        h2 = H + H
        print("{:.2f}".format(h2))
    elif n == 3:
        h3 = H + H + H / 2
        print("{:.2f}".format(h3))
    elif n == 4:
        h4 = H + H + H / 2 + H / 4
        print("{:.2f}".format(h4))
    elif n == 5:
        h5 = H + H + H / 2 + H / 4 + H / 8
        print("{:.2f}".format(h5))
