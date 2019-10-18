import re
# # 使用match方法进行匹配操作
# result = re.match("[1-47-8]\s\w\d\s\w.\w\w","8 e9 guol")
# # 如果上一步匹配到数据的时候，可以使用group方法来提取数据
# result.group()
# print(result)
# print(result.group())
#
# result1 = re.match("[第]\d....\d....弟","第1个人是第2个人的弟弟")
# print(result1.group())
# print(result1)
# result2 = re.match("\D[2]\D.\D.[3].....","第2个人是第3个人的哥哥")
# print(result2.group())
#
# result3 = re.match("[A-Z][a-z]+","AbcdA")
# print(result3.group())
#
# list_li = ["name","Name","_name1","name_2","2_name2","_name_"]
# for li in list_li:
#     result4 = re.match("[A-Za-z_]+[\w]*",li)
#     if result4:
#         print("匹配成功：%s" %result4.group())
#     else:
#         print("变量名非法：%s" %li)

# r = re.match("[1-9]?\d+","3333")
# print(r.group())



# list_li = ["heldwwwlo@246.com","hedddlglo@469.com","hello@163.com","hello@163.comwww"]
# # for li in list_li:
# #     r2 = re.match("[\w]{4,20}@163\.com$",li)
# #     if r2:
# #         print("匹配成功：%s" %r2.group())
# #     else:
# #         print("false： %s" %li)
#
# ret = re.match("[1-9]?\d$|100","100")
# print(ret.group())
#
list_li = ["test@126.com","test@qq.comeeeee","test@163.com","2bcdf@227.comdd"]
for li in list_li:
    r = re.match("\w{4,20}@(126|163|qq)\.com$",li)

        print("false %s" %li)
#
# tels = ["13100001234", "18912344321", "10086", "18800007777"]
# for t in tels:
#     r = re.match("1\d{9}[0-35-68-9]",t)
#     if r:
#         print("s :%s" %r.group())
#     else:
#         print("f :%s" %t)

# r = re.match("([^-]*)-(\d+)","0938-123456789")
# print(r)
# print(r.group())
# print(r.group(1))
# print(r.group(2))
#
# # "<html>hh</html>"
# r1 = re.match(r"<([a-zA-Z]*)>\w*</\1>","<html>hh</html>")
# print(r1.group())
# labels = ["<html><h1><h2><h3>www.itcast.cn</h3></h2></h1></html>", "<html><h1>www.itcast.cn</h2></html>"]
# for la in labels:
#     r = re.match(r"<(\w*)><(\w*)><(\w*)><(\w*)>.*</\4></\3></\2></\1>",la)
#     if r:
#         print("s :%s" %r.group())
#     else:
#         print("f :%s" %la)

# labels2 = ["<html><h1><h2><h3>www.itcast.cn</h3></h2></h1></html>",
#            "<html><h1>www.itcast.cn</h1></html>",
#            "<html><h1>www.itcast.cn</h2></html>"]
#
# for l in labels2:
#     r = re.match(r"<(?P<guo1>\w*)><(?P<guo2>\w*)>.*</(?P=guo2)></(?P=guo1)>",l)
#     if r:
#         print("true: %s" %r.group())
#     else:
#         print("false: %s" %l)
#
# r2 = re.search("\d+","阅读的数量 73333")
# print(r2.group())
# r3 = re.findall("\d+","python = 2999,python = 39444,c++ =8887")
# print(r3)
# r4 = re.sub("\d+","899","python = 898")
# print(r4)
# def add(temp):
#
# #     num = temp.group()
# #     print("num=%s" %num)
# #     num2 = int(num)+1
# #     return str(num2)
# # rr = re.sub(r"\d+",add,"python = 1999")
# # print(rr)
# #
# #
# #
# # r4 = re.split(";| ","info;li 22 shangdonng")
# # print(r4)
# li = ["https://rpic.douyucdn.cn/live-cover/appCovers/2019/08/05/7155992_20190805013248_small.jpg/dy1",
#       "rs16""https://sta-op.douyucdn.cn/dy-listicon/5c1311119b5fdd7880fa6d6c6032b6ad.png","https://rpic.douyucdn.cn/live-cover/roomCover/2019/08/01/7b27c154141ccad72d296c1aba7af77d_big.jpg/dy1"
#       ,"https://rpic.douyucdn.cn/asrpic/190808/4902933_6209176_3701f_2_big.jpg/dy1"
#        "page_type""month", "page_title" "主播月榜" "name" "颜值榜单" "page_more_btn_title" "更多"
#     ]
# for a in li:
#     r3 = re.findall(r"[rs16]://.*?_big.jpg/dy1",a)
#     if r3:
#         print(r3)
#     else:
#         pass
#
