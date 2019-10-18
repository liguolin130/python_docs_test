# 1.水仙花数字
# for number in range(100,1000):
#     one = number%10
#     two = number%10//10
#     three = number//100
#     if (one**3)+(two**3)+(three**3) == number:
#         print("水仙花数:%s\n" %number)

# 2.验证三次出入机会
# counter = 3
#
# while counter:
#     pass_word = input("请输入密码")
#     if pass_word == "123":
#         print("登陆成功")
#         break
#     elif "*" in pass_word :
#         print("密码中包含*请重新输入")
#         continue
#     else:
#         print("密码错误")
#         counter -=1
#         continue
# if counter == 0:
#     print("次数已用完")

# 判断闰年
# year=int (input(":"))
# if (year % 4 ==0) or (year % 400 ==0):
#     print("%s是闰年/n" %year )
# else:
#     print("s")

# 生成器 ,列表生成器的方括号换成圆括号，再遍历一次最后使用naxt（）函数调用

a = (x**2 for x in range(4))
for c in range(4):
    print(next(a))


# # 奇数生成器
# def odd():
#     a = 1
#     while True:
#         yield a
#         a += 2
# num_odd = odd()
# counter = 0
# for b in num_odd:
#     if counter >= 100:
#         break
#     print(b)
#     counter +=1
#


#
# def fun(a,b):       # 函数的嵌套
#     def fun_in(x):
#         return a*x+b
#     return fun_in    # 返回内部函数
# f = fun(2,3)
# print("结果=%d" %f(4)) # 内部函数test_in传参
#
# def demo_without(fun):
#     def demo_inside():
#         print("one")
#         fun()
#     return demo_inside
# def test():
#     print("two-test")
#
# f = demo_without(test)
# f()

# import socket
#
#
#
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.close()
# a = list(filter(None,[0,1,2,3,0,0]))
# print(a)
# globals()
# locals()

# print("ab" in  "abced")
# def wrapper(func):
#     def inner(*args,**kwargs):
#         func(*args,**kwargs)
#     return inner
# @wrapper
# def a(arg):
#     print(arg)
# a(33)

