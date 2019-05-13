"""
建立一个角类，在这个类中重载减号运算符（角度相减），
并实现求出角度的正弦值的函数。
"""
import math


def fun1():
    n = int(input())
    for i in range(n):
        temp1, temp2 = input().split()
        print("{:.2f}".format(math.sin(math.pi * ((int(temp1) - int(temp2)) / 180))))


def fun2():
    """
    链接：https: // www.nowcoder.com / questionTerminal / 7
    b1e4ffc39604be3b15959ce329da490
    来源：牛客网
    """
    m = int(input())
    for i in range(m):
        temp = list(map(int, input().split()))
        print('%.2f' % (math.sin(math.pi * (temp[0] - temp[1]) / 180)))


"""
input是str类型；
split默认是空格；
{}和:可以代替%；
sin要求里面是弧度值；

map使用，一个函数，另一个序列；
map返回的是map类型的，用list强制转格式
"""
