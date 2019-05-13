"""
给定一个无序数组，包含正数、负数和0，要求从中找出3个数的乘积，使得乘积最大，要求时间复杂度：O(n)，空间复杂度：O(1)
"""
lis = list(map(int, input().split()))
lis = sorted(lis)
l = len(lis)
if lis[0] < 0 and lis[1] < 0:
    temp_1 = lis[0] * lis[1] * lis[l - 1]
    temp_2 = lis[-1] * lis[-2] * lis[-3]
    print(temp_1 if temp_1 > temp_2 else temp_2)
else:
    temp_2 = lis[-1] * lis[-2] * lis[-3]
    print(temp_2)
"""
运行自己输入的案例还可以，但是满足时间复杂度这个不会，先放着，这个是拼多多的题目，和之前的题目不太一样了
"""