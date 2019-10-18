'''
函数功能：新增，查询，修改，删除
'''
card_list = [] # 记录所有名片的列表

def show_menu():
    print("*"*50)
    print("欢迎使用【名片管理系统】V1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("4.修改/删除/返回主菜单")
    print("")
    print("0.退出系统")
    print("*"*50)

def new_card():
    print("-"*50)
    print("功能：新建名片")
    print("")
    name = input("请输入姓名:")
    tel = input("请输入电话号码:")
    qq = input("请输入qq号码:")
    email = input("请输入邮箱:")
    # 将名片保存到字典里
    card_dictionary ={"name":name,"tel":tel,"qq":qq, "email":email}
    print("成功添加%s的名片" % card_dictionary["name"])

    card_list .append(card_dictionary)  # 将字典放到列表里
    print(card_list)

def show_all():
    print("*"*50)
    print("功能：显示全部")
    print("")
    for name in ["姓名","电话","qq","邮箱"]:
        print(name,end="\t\t" )
    print("")
    for card_dictionary in card_list:
        print("%s\t\t%s\t\t%s\t\t%s\t\t" %(card_dictionary["name"],
                                           card_dictionary["tel"],
                                           card_dictionary["qq"],
                                         card_dictionary["email"]))

    if len(card_list) == 0:
        print("没有加入名片")
        return
def search_card():
    print("-"*50)
    print("功能：搜索名片")
    search_name = input("请输入要查找的人")
    for card_dictionary in card_list:
        if card_dictionary["name"] == search_name:
            print("%s\t\t%s\t\t%s\t\t%s\t\t"
                  %(card_dictionary["name"],card_dictionary["tel"],
                    card_dictionary["qq"],card_dictionary["email"]))
            break
        else :
            print("没有找到%s" %search_name)

def deal_card(find_dictionary):
    print(find_dictionary)
    action_str = input("请输入要要执行的操作，1修改，2删除，0返回上一层菜单:")
    if action_str == "1":
        find_dictionary["name"] = input("请输入姓名：")
        find_dictionary["tel"] = input("请输入电话号码：")
        find_dictionary["qq"]= input("请输入qq号码：")
        find_dictionary["email"] = input("请输入邮箱")
        print("%s的名片修改成功" %find_dictionary["name"])
    elif action_str == "2":
        card_list.clear()
        print("%s的名片已经删除"%card_list)
    elif action_str == "0":
        return
def input_cards_info(dictionary_value,tip_massage): # tip_massage 输入提示信息
    result_str = input(tip_massage)
    if result_str > 0:
        return tip_massage
    else :
        return dictionary_value


