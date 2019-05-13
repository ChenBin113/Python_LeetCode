"""
写一个类，能接受int 型的变量，接收变量后能存储原变量（譬如12345）和其反向变量(54321)，
最多处理数量为10 个，当输入达到10 个或者输入变量为0 的时候停止。
并且在类销毁前输出存储的所有变量。
"""
"""
第一种：编译器可以通过
temp = input()
lis = temp.split()
if lis[-1] == '0':
    lis.pop()
if len(lis) > 10:
    lis = lis[:10]
for i in lis:
    j = int(i[::-1])
    print("{0} {1}".format(i,j))
"""
for i in range(10):
    temp = input()
    if temp == '0':
        break
    else:
        j = int(temp[::-1])
        print("{0} {1}".format(temp, j))

"""
之前写的可以运行得到结果，但是在线上会出错，看了别人的输入模式，修改一下就可以在线上通过
"""
