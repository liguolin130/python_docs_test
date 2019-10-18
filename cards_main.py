import cards_tools
flage = True
while 1:
    cards_tools.show_menu() #引入欢迎界面模块
    action = input("请选择输入功能:")
    print("您选择的操作是:%s" %action)
    if action in ["1","2","3","4"]: # in针对列表，可以避免输入的不是数字
        if action =="1":
            cards_tools.new_card()
        elif action =="2":
            cards_tools.show_all()
        elif action =="3":
            cards_tools.search_card()
        elif action == "4":
            cards_tools.input_cards_info("李","false")
    elif action == "0":
        flage = False
    else:
        print("input false ,please ")



