# # 字符串的方法
# string = "56278920331 45"
# string2 = "223"
# str = ["ji","h","i"]
#
# string1 = "jigyguyg"
# def demo():
#     a=string.title() # 将单词的首字母大写
#     print(a)
#     b=string.lower()# 将所有的大写字母转换为小写字母
#     print(b)
#     c=string.upper() #将所有的小写字母转换为大写字母
#     print(c)
#     d=string.strip()# 截去string左右两边的空白字符串
#     print("s==%s"%d)
#     e=string.split("e")
#     print(e)
#     # f=string[::-1]# 字符串的逆序输出[::-1]
#     # print("切片==%s"%f)
#     e= string[::-3]
#     print("e=%s"%e)
#     print(string1+string)
#     print(["-"*5])
#     print("a" not in string1)
#     print(string>=string2)
#
#     for name in string2:
#         print(name)
#         if name == "8":
#             print("找到啦")
#             break
#         else:
#             print("没有找到!")
#     print("程序结束")
#


# print(len(string)) #计算容器的元素个数
# print(max(string))  #返回容器元素最大值

#     print(a)
#    # string.count("h","d",3)
#     #print(string)
#     # b= string.isspace()

# 排序方法一
s = [('牛牛', 'A', 15), ('到', 'B', 12), ('大', 'B', 13), ('大', 'B', 20)]
for i in  range(len(s)):
    for j in range(len(s)):
        if s[j][2]>s[i][2]:
            s[j],s[i]=s[i],s[j]
print(s)

# 排序方法二
# b=[]
# for i in range(len(s)):
#     a=s[i][2]
#     # print(a)
#     b.append(a)
# # print(b)
# c=sorted(b)
# # print(c)
# for i in c:
#     for j in range(len(s)):
#         if s[j][2]==i:
#             print(s[j])

# aa = (a*a for a in range(4))
# print(next(aa ))
# print(next(aa))


# import re
# s = 'asn3nj46k7j8j3h2h'
# aa = re.findall("(\d)",s)
# print(aa)

#
# str1 = 'k:1|k1:2|k2:3|k3:4' # {K:1,}
# li = str1.split("|")
# di = None
# for i in li:
#     for k,v in i.split(":"):
#         di[k]=v
# print(di)

