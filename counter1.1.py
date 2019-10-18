# counter
# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b
# a = int(input("input first number："))
# c = int(input("1=+，2=-，3=*，4=/："))
# b = int(input("input second number："))
#
# if c ==1:
#     print(add(a,b))
# elif c==2:
#     print(subtract(a,b))
# elif c==3:
#     print(multiply(a,b))
# elif c==4:
#     print(divide(a,b))
# else:
#     print("非法输入")

"""
判断素数的上限最准确的应该使用平方根取整加一
"""
import math
for a in range(2,101):
    for b in range(2,int(math.sqrt(a))+1):
        if a%b== 0:
            break
    else:
        print(a)

# print(list(range(6)[::2]))
# 'ab' in 'abcde'
print('\n'.join(['\t'.join(["%2s*%2s=%2s"%(j,i,i*j) for j
                            in range(1,i+1)]) for i in range(1,10)]))