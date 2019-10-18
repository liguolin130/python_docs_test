#  # 计算创建的对象总数
# class Tool(object):
#     counter = 0
#     def __init__(self,name):
#
#         self.name = name
#         Tool.counter += 1
# tool1 = Tool("gg")
# tool2 = Tool("dd")
# tool3 = Tool("ddr")
# print("创建的对象有%s个" %Tool.counter)
#
# class Tool(object):
#     counter = 0
#     def __init__(self,name):
#         self.name = name
#         cls.counter += 1
#     @classmethod
#     def show_tool_counter(cls):
#         print("创建了%d个对象" %cls.counter)
# Tool.show_tool_counter()
#
#
#
# class Game(object):
#     top_score = 0  # 类属性记录游戏最高分
#     def __init__(self,player_name):
#         self.player_name = player_name
#     @staticmethod  # 申明是静态方法
#     def show_help():
#         print("GAME HELP")
#     @classmethod # 申明是类方法
#     def show_top_score(cls):
#         print("max is %d" %cls.top_score)
#     def start_game(self):
#         print("%s开始游戏" %self.player_name)
#         Game.top_score = 1000
# Game.show_help()
# # Game.show_top_score()
# player = Game("li")  # 创建游戏对象
# player.start_game()
# Game.show_top_score()
#

#
# from close_packge import persondd
# obj = persondd()
# print(obj.__module__)
# print(obj.__class__)
#
#
#










import time
import os
import re

template_root = "./templates"

# ----------更新----------
# 用来存放url路由映射
# url_route = {
#   "/index.py": index_func,
#   "/center.py": center_func
# }
g_url_route = dict()

# ----------更新----------
def route(url):
    def func1(func):
        # 添加键值对，key是需要访问的url，value是当这个url需要访问的时候，需要调用的函数引用
        g_url_route[url] = func
        def func2(file_name):
            return func(file_name)
        return func2
    return func1


@route("/index.py")  # ----------更新----------
def index(file_name):
    """返回index.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        data_from_mysql = "暂时没有数据，请等待学习mysql吧，学习完mysql之后，这里就可以放入mysql查询到的数据了"
        content = re.sub(r"\{%content%\}", data_from_mysql, content)

        return content


@route("/center.py")  # ----------更新----------
def center(file_name):
    """返回center.py需要的页面内容"""
    # return "hahha" + os.getcwd()  # for test 路径问题
    try:
        file_name = file_name.replace(".py", ".html")
        f = open(template_root + file_name)
    except Exception as ret:
        return "%s" % ret
    else:
        content = f.read()
        f.close()

        data_from_mysql = "暂时没有数据,,,,~~~~(>_<)~~~~ "
        content = re.sub(r"\{%content%\}", data_from_mysql, content)

        return content


def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-Type', 'text/html')]
    start_response(status, response_headers)

    file_name = environ['PATH_INFO']
    # ----------更新----------
    try:
        return g_url_route[file_name](file_name)
    except Exception as ret:
        return "%s" % ret










