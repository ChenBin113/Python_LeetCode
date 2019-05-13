"""
根据输入的字符串判断字符串中数字的位置。
输入第一行表示测试用例的个数m，接下来m行每行以个字符串，字符串长度不超过50。
输出m行。每行输出一行数字，用空格隔开，按顺序表示字符串中出现的数字的位置。
输入
1
a3b4c5
输出
2 4 6
"""
lis_num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
m = int(input())
for i in range(m):
    string_num = input()
    lis_pos = []
    for pos in range(len(string_num)):
        if string_num[pos] in lis_num:
            lis_pos.append((pos + 1))
    for j in lis_pos:
        print(j, end=' ')
    print()

# 他人写法
m = int(input())

for i in range(m):
    lst = input()
    out = []
    num_lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for j in range(len(lst)):
        if lst[j] in num_lst:
            out.append(j + 1)
    print(' '.join(map(str, out)))

"""
最后这句写得很值得学习，简洁：map我是会的，但是不敢用的，接触了这么多次，要多学习，join也是学过的
"""
