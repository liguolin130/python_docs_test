
#1. # 闭包
# # 嵌套函数（要素一）
# def test(num):
#     def test_in(num_in):
#         # 内部函数对外部函数的引用
#         print("sum=%s" %(num+num_in))
#         # 返回结果可以被打印出来
#         return num,num_in
#     # 返回内部函数（要素三）
#     return test_in
# # rtn就是test_in
# rtn = test(10)
# print(rtn)
# # 内部函数test_in传参
# print(rtn(20))


# 2.函数名仅仅是变量,只不过指向了定义的函数而已,所以才能通过函数名()调用,如果函数名=
#xxx被修改那么当在执行函数()

# 3. 闭包的一个实际应用
# def line_conf(a,b):
#     def lin(x):
#         return a*x+b
#     return lin
# line1 = line_conf(2,3)
# line2 = line_conf(3,4)
# print("第一个数==%d" %line1(4))
# print("第二个数==%d" %line2(5))

# 4.修改外部函数变量
# def conter(num):
#     def incr():
#         nonlocal num
#         num += 1
#         return num
#     return incr
# c1 = conter(2)
# print(c1())
# print(c1())
# print(c1())
# c2 = conter(10)
# print(c2())
# print(c1())
# print(c2())

# 装饰器
#定义函数包裹数据
# def makeBoid(fn):
#     def warppad():
#         return "<b>" +fn()+"</b>"
#     return warppad
# def makeItalik(fn):
#     def warppad():
#         return "</b>"+fn()+"<b>"
#     return warppad
#
# # 装饰一下makeBoid()
# @ makeBoid
# def test1():
#     return "hello world"
# @ makeItalik
# def test2():
#     return "guolin"
#
# # 用一个装饰器同时装饰两个函数
# @makeBoid
# @makeItalik
# def test3():
#     return "liguolin--3"
# print(test1())
# print(test2())
# print(test3())

# 示列
# 1.被装饰的函数没有参数
# from time import ctime,sleep
# def timefun(fun):
#     def warddad():
#         print("(%s) called at(%s) " %(fun.__name__,ctime))
#         fun()
#     return warddad
# @ timefun
# def time():
#     print("i am timefun")
# time()
# sleep(1)
# time()
# print(time())

# 2.被装饰的函数有参数
# from time import ctime,sleep
# def timefun(fun):
#     def warppad(a,b):
#         # print("(%s)called at (%s)" %(fun.__name__,ctime))
#         fun(a,b)
#     return warppad
# @ timefun
# def test(a,b):
#     print("sun==%s" %(a+b))
# test(2,3)
# sleep(1)
# test(3,4)

# 被装饰的函数参数是不定长参数
# from time import ctime,sleep
# def time_funs(fun):
#     def warppad(*args,**kwargs):
#         print("%s called at %s" %(fun.__name__,ctime))
#         fun(*args,**kwargs)
#     return warppad
# @ time_funs
# def test(a,b,c):
#     print("sum==%s" %(a+b+c))
# test(1,2,3)
# sleep(1)
# test(2,3,4)
#


# 装饰器的return
# from time import ctime,sleep
# def funtime(fun):
#     def warppad():
#         print("((%s) called at (%s)" %(fun.__name__,ctime))
#         fun()
#     return fun
# @ funtime
# def test():
#     print("I am test")
# @ funtime
# def foo():
#     return "haha"
# test()
#
# print(foo())


# 装饰器带有参数,在原有装饰器的基础上,设置外部变量
# from time import ctime,sleep
# def fun_arg(pe="hello"):
#     def funtime(fun):
#         def warrddap():
#             print("%s called at %s %s" %(fun.__name__,ctime,pe))
#             fun()
#         return warrddap
#     return funtime
# @ fun_arg("python")
# def test():
#     print(" I am fun_arg")
# @ fun_arg("java")
# def foo():
#     print("I am foo")
# test()
# sleep(1)
# test()
#
# foo()
# sleep(1)
# foo()

# 装饰器函数其实就是这样一个接口约束,他必须接受一个callable对象作为参数,必须返回一个callable对象


class persondd(object):
    def __init__(self):
        self.name = 'li'