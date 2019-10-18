from functools import reduce
# #
# # list_1_10 = [x**2 for x in range(1,11)]
# # print("平方=%s" %list_1_10)
# #
# # list_1_10_ou = [x**2 for x in range(1,11) if x%2 == 0]
# # print("偶数平方=%s" %list_1_10_ou)
# #
# # # 多重嵌套里面的数是2的倍数的平方组成的列表
# # list1 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# # list2 = [b**2 for a in list1 for b in a if b%2 == 0]
# # print("多重嵌套=%s" %list2)
# #
# # # 多重嵌套中的以重的列表长度大于一
# # list1 = [[1,2,3],[4,5,6],[7,8,9],[10]]
# # list3 = [b**2 for a in list1 if len(a)>1 for b in a if b%2 == 0]
# # print("多嵌套中的一重=%s" %list3)
# # print((lambda a : a*a)(3))
# # a = lambda a:a*a
# # print(a(3))
# # print([(lambda a:a*a)(a) for a in range(11)])
# #
# # aa = map(lambda a:a%2 ==0 ,range(10))
# # for i in aa:
# #     print(i)
# #
# # print(reduce(lambda  x ,y:x+y,range(1,101)))
# #
# #
# # print([i%2 for i in range(10)])

# import json
# class student(object):
#     def __init__(self,name,age,course):
#         self.name = name
#         self.age = age
#         self.course = course
# a = student("guo",14,"xixi")
# b = json.dumps(a)
# print(b)
#file = open("file")

# # 2. 读取
# text = file.read()
# print(text)
#
# # 3. 关闭
# file.close()
#

import pickle
d = [1,5,4,5,6]
a=pickle.dumps(d)
print(a)
b= type(pickle.dumps(d))
print(b)

# json表示出来就是一各字符串
import json
d = [1,2,3,4]
a =json.dumps(d)
print(a)
b = type(json.dumps(d))
print(b)
