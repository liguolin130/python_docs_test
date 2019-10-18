class Dog(object):
    def __init__(self,name):
        self.name = name
    def game(self):
        print("%s只是玩耍" %self.name)

class XiaoTianDog(Dog):
    def game(self):
        print("%s在天上玩耍" %self.name )

class person(object):
    def __init__(self,name):
        self.name = name
    def person_and_dog(self,dog):
        print("%s 和%s快乐的玩耍" %(self.name,dog.name))
        dog.game()
        

wangwang = Dog("旺旺")

dahuang = XiaoTianDog("supper dog")

li = person(" guolin") # 创建对象

 # li对象调用和够玩耍的方法
li.person_and_dog(dahuang)
