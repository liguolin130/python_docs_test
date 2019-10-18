class HouseItem:

    def __init__(self,name,area):
        self.name = name
        self.area = area

    def __str__(self):
        return "[%s]占地面积%.2f" %(self.name,self.area)

bad = HouseItem("席梦思", 4)
chest = HouseItem("衣柜", 2)
table = HouseItem("餐桌", 1.5)
print(bad)
print(chest)
print(table)


class House:

    # 初始化
    def __init__(self,house_type,area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.list_item = []

    def __str__(self):
        return ("户型：%s\n总面积：%.2f[%.2f]\n家具：%s"
                %(self.house_type,self.area,self.free_area,self.list_item))

    def add_item(self,item):
        print("要添加%s" %item)
        if item.area > self.free_area:
            print("%s的面积太大不能添加到房子中" %item.name)
            return
        self.list_item.append(item.name)
        self.free_area -= item.area

my_house = House("两室一厅", 65)
# 将家具添加到房子
my_house.add_item(bad)
my_house.add_item(chest)
my_house.add_item(table)
print(my_house)
