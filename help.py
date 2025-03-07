def helps(): 
    helps_list=[
        "可用指令：",
        "help : 显示帮助信息 (指令列表)",
        "look : 查看当前房间的详细描述。",
        "go [⽅向] : 向指定⽅向移动 (例如: north, south, east, west, down)。",
        "take [物品名称] : 拾取房间内的物品。",
        "inventory : 查看背包中的物品。",
        "quit : 退出游戏。"]
    for help in range(len(helps_list)):
        print(helps_list[help])
if __name__=="__main__":
    helps()