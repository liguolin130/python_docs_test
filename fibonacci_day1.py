
# #生成器函数生成斐波那契数
def fibonacci(time):
    a = 0
    b,c = 0,1
    while a<time:
        yield c
        b,c = c,b+c
        a += 1
    return
f =fibonacci(10)
for d in f:
    print(d)
# 方法二
def fibonacci(d):
    counter = 0
    a,b = 1,1
    for c in range(d):
        counter +=1
        print("第%d个数列：%d"  %(counter,a))
        a,b = b,a+b
    return a
result = fibonacci(10)


# 生成器来实现斐波那契数列

# def Fibonacci(s):
#     counter = 0
#     num1,num2 = 1,1
#     while counter < s:
#         num = num1
#         num1,num2 = num2,num1+num2
#         counter += 1
#         yield num
#     return "guo"
# f = Fibonacci(5)
# while True:
#     try:
#         a = next(f)
#         print("value = %d" %a)
#     except StopIteration as b :
#         print("生成器返回值 %s" %b.value)
#         break
li=[1,2,3,0,14]
for a in li:    
    li.remove(a)
print(li)