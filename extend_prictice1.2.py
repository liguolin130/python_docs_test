'''
"""
编写函数模拟内置函数sum（），实现值相加输出
"""""
def sum(c):
    a = 0
    for b in c:
        a += b
    return  a
d = range(1,5)
result = sum(d)
print("内置函数相加=%d" %result)
# d = [1,2,3,4]
# print(sum(d))


"""
 编写函数，可以任意接收多个整数并可以输出其中的最大值和所有整数之和
 *arge(不定长参数传不了range())传不了range()
"""
def demo(*args):
    max_m = max(args)
    a = 0
    for b in args:
        a += b
    return a,max_m
result = demo(1,2,6)
print("result=%d\nmax=%d" %result)


"""
斐波那契数列
1,1,2,3,5,8,13,21
"""

d


"""
检查元素是否有空内容（函数加字符串的检查方法）
"""
def demo(v):
    flag = True
    for a in v:
        if a.isspace():
            flag = False
            break
    return flag
result1 = demo("1,2  4,56")
print("是否有空白字符：%s" %result1)


"""
计算传入字符串的数字，字母，空格以及其他的个数
"""
def demo(v):
    number = 0
    letter = 0
    space = 0
    other = 0
    for a in v:
        if a.isdigit()==True: # 判断是否是数字组成的方法
            number +=1
        elif a.isalpha()==True:# 判断是否是字母组成的方法
            letter += 1
        elif a.isspace()==True:# 判断是否有空格组成的方法
            space +=1
        else:
            a.other +=1
    return (number,letter,space,other)
result = demo("13 a c3")
print(result)
'''




