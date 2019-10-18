
# 私有化
# class Person(object):
#
#     def __init__(self,name,age,test):
#         self.name = name
#         self._age  = age
#         self.__test = test
#
#     def showperson(self):
#         print(self.name)
#         print(self._age)
#         print(self.__test)
#
#     def dowork(self):
#         self._work()
#         self.__away()
#
#     def _work(self):
#         print("my_work")
#
#     def __away(self):
#         print("my__away")
#
#
#
# class student(Person):
#     def constraction(self,name,age,taste):
#         self.name = name
#         self._age = age
#         self.__taste = taste
#
#     def showstudent(self):
#         print(self.name)
#         print(self._age)
#         print(self.__taste)
#
#     @ staticmethod
#     def testbug():
#         _Bug.showbug()
#
# class _Bug(object):
#
#      @ staticmethod
#      def showbug():
#         print("showbug")
#
# s1 = student("guo",18,"playbassketball")
# s1.showperson()
# print("-"*20)
#
# s1.constraction("jia",18,"playgame")
# s1.showstudent()
# print("-"*20)
#
# s1.showstudent()
# print("-"*20)
#
# student.testbug()

# 多态
class MiniOS(object):
    def __init__(self,name):
        self.name = name
        self.apps = []
    def __str__(self):
        return "%s 安装的软件列表为%s" %(self.name,str(self.apps))

    def install_app(self,app):
        if app.name in self.apps:
            print("已经安装了软件：%s，不需要再安装" %app.name)
        else:
            app.install()
            self.apps.append(app.name)

class App(object):
    def __init__(self,name,version,desc):
        self.name = name
        self.version = version
        self.desc = desc

    def __str__(self):
        return "%s当前的版本是%s-%s" %(self.name,self.version,self.desc)
    def install(self):
        return "将%s[%s]的执行程序复制到程序目录" %(self.name,self.version)

class Pycharm(App):
    pass

class Chrome(App):
    def install(self):
        print("正在解压缩安装程序。。。")
        super().install()

linux = MiniOS("Linux")

pycharm = Pycharm("pycharm","1.0","huanjinlkaifa")
chrome = Chrome("charom","2.0","guge")
print(linux)
linux.install_app(pycharm)
linux.install_app(chrome)
linux.install_app(chrome)
print(linux)




