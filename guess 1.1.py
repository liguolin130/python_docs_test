'''
输入1-100的数字，50-60是正确的
输入五次后退出系统
'''
counter = 0
while counter <5:
    user_name = int(input("请输入1—100之间的数:"))
    if user_name>=50 and user_name<=60:
         print("congratulation,guess true!")
         break
    elif user_name <=40 and user_name >=0:
        print("尝试输入较大的数值")
    elif user_name >= 70 and user_name <= 100:
        print("尝试输入数值较小的数字")
    elif ((user_name >40 and user_name < 50) or (user_name> 60 and user_name < 70)):
        print("您输入的值很接近了")
    else :
        print("您输入的数字超出了范围")
    counter +=1



# 日历
year = int(input("please search year:"))
month = int(input("please search month:"))
month_max_31 = [1,3,5,7,8,10,12]
month_min_30 = [2,4,6,9,11]
flag = True

sum = 0
# 返回True为闰年356天
def is_run(year):
    global  flag
    if (year%4 == 0 and year%100 !=0) or year%400== 0:
        flag=flag
    else:
        flag =False
    return flag

# 判断大小月份
def month_choise(m):
    if m in month_max_31:
        return 31
    elif m in month_min_30:
        return 30
    elif is_run(year):
        return 29
    else:
        return 28
# 遍历从1990——input的年份
for y in range(1990,year):
    if is_run(year):
        sum +=366
    else:
        sum += 365
# 遍历1月份到input
for m in range(1,month):
    if m in month_max_31:
        sum += 31
    elif m in month_min_30:
        sum +=30
    elif is_run(year):
        sum +=29
    else:
        sum +=29
    #print(sum)
print()
print("-"*50)
print("日\t一\t二\t三\t四\t五\t六")

counter = 0
counter +=(sum+1)%7

for i in range(counter):
    print("\t",end="")
for m_y in range(1,month_choise(month)+1):
    print(str(m_y)+"\t",end="")
    counter += 1
    if counter%7 ==0:
        print()


# 此包的功能是随即输出a，b之间的数字以及本身的数
import random
computer = random.randint(1,3)
person = input("猜拳：石头（1），剪刀（2），布（3）:")
if ((computer == 1 and person == 3) or
        (computer == 2 and person == 1) or
        (computer == 3 and person == 2)):
    print("voctory")
elif computer == person :
    print("draw")
elif ((computer == 3 and person == 1) or
        (computer == 2 and person == 3) or
        (computer == 1 and person == 2)):
    print("To lose")
else :
    print("try again")

    a = 3  # 计数器
    flage = True  # 设置一个标签，在要退出的时候false
    counter = 0
    while counter < 5:
        user_name = int(input("请输入账号："))
        usre_pass = input("请输入密码：")
        if user_name == 1 and usre_pass == 1:
            print("登陆成功！Welcome！")
            print("@@@" * 50)
            print("0.返回上一层")
            print("1.查询所有商品：")
            print("2.分类商品查询：")
            print("3.查询商品品牌：")
            print("=" * 50)

            # close_type = input("请输入选择类型：")
            # if close_type== "1" :
            #     continue
            # elif close_type == "2":
            #     print("选择A or B or C")
            #     commodity = input("输入A or B or C查看各自信息：")
            #     if commodity == "A":
            #         print("This is a")
            #     else :
            #         print("false")
            #     if commodity == "B":
            #         print("This is b")
            #     else :
            #         print("false")
            #     if commodity == "C":
            #         print("This is c")
            #     else :
            #         print("false")
            # elif close_type == "3":
            #     print("选择 iphon or xiaomi or huawei:")
            Exit = input("输入exit退出程序:")
            if Exit == "exit":
                break
        else:
            a -= 1
            print("剩余次数：%d" % a)  #
            if a == 0:
                b = input("您输入的次数大于三次是否继续尝试，输入Y/y可继续")  # 返回值是str型
                if b == "y" or b == "Y":
                    a = 3
                    continue


                else:
                    print("report Y/y")
                    break
        counter += 1
