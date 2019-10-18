# try:
#     num = int(input("请输入一个整数"))
# except:
#     print("请重新输入")

# try:
#     num = int(input("请输入整数"))
#     result = 8/num
#     print(result)
# except ValueError:
#     print("请输入正确的整数")
# except ZeroDivisionError:
#     print("除以0错误")
# except Exception as result:
#     print("未知错误%s" %result)
# else:
    # 没有异常才会执行
#     pass
# finally:
#     print("正常执行，，但是不保证正确")
#     pass

# 定义函数demo1() 提示用户输入一个整数并且返回
# 定义函数demo2（）调用demo1（）
# 在主程序中调用demo2（）
# def demo1():
#     return int(input("请输入整数"))
# def demo2():
#     return demo1()
# try :
#     print(demo2())
# except ValueError:
#     print("请输入正确的整数")
# except Exception as result:
#     print("unknown error%s" %result)

def input_password():
    pwd = input("请输入八位密码")
    if len(pwd) >= 8:
        return pwd
    # 创建异常对象，使用异常的错误信息字符串作为参数
    ex = Exception("密码长度不够")
    raise ex
try:
    user_pwd = input_password()
    print(user_pwd)
except Exception as result:
    print("未知错误%s"  %result)




