# 定义房间和初始状态
rooms = {
    "Foyer": {
        "description": "你身处古堡的阴暗⻔厅。头顶⼀盏布满蜘蛛⽹的吊灯微微摇晃，投下忽明忽暗的光芒。",
        "exits": {"north": "Grand Hall", "east": "Hallway"},
        "items": ["钥匙"]
    },
    "Grand Hall": {
        "description": "你进入了古堡的宏伟大厅。彩⾊玻璃窗阻挡了外界的光线，使得⼤厅内光线昏暗。",
        "exits": {"south": "Foyer", "west": "Library", "east": "Dining Room"},
        "items": []
    },
    "Hallway": {
        "description": "你沿着昏暗的⾛廊前⾏，脚踩在吱吱作响的⽊地板上。",
        "exits": {"west": "Foyer"},
        "items": ["手电筒"]
    },
    "Library": {
        "description": "你进入了布满灰尘的图书馆。⾼耸的书架⼀直延伸到天花板。",
        "exits": {"east": "Grand Hall"},
        "items": ["古老的书"]
    },
    "Dining Room": {
        "description": "你来到了宽敞的餐厅。⻓⻓的橡⽊餐桌上布满了厚厚的灰尘。",
        "exits": {"west": "Grand Hall", "north": "Kitchen"},
        "items": []
    },
    "Kitchen": {
        "description": "你进入了阴冷潮湿的厨房。腐烂的⽓味扑⿐⽽来。",
        "exits": {"south": "Dining Room"},
        "items": ["匕首"]
    }
}

# 玩家初始状态
player = {
    "current_room": "Foyer",  # 初始房间
    "inventory": []  # 初始背包为空
}

# 显示当前房间信息
def look():
    room = rooms[player["current_room"]]
    print(room["description"])
    if room["items"]:
        print("房间内的物品:", ", ".join(room["items"]))
    print("可前往的方向:", ", ".join(room["exits"].keys()))

# 移动到另一个房间
def go(direction):
    room = rooms[player["current_room"]]
    if direction in room["exits"]:
        player["current_room"] = room["exits"][direction]
        print("你前往了", player["current_room"])
        look()
    else:
        print("你不能往那个方向走。")

# 拾取物品
def take(item):
    room = rooms[player["current_room"]]
    if item in room["items"]:
        player["inventory"].append(item)
        room["items"].remove(item)
        print("你拾取了:", item)
    else:
        print("这里没有", item)

# 查看背包
def inventory():
    if player["inventory"]:
        print("你的背包中有:", ", ".join(player["inventory"]))
    else:
        print("你的背包是空的。")

# 使用物品
def use(item):
    if item in player["inventory"]:
        if item == "钥匙" and player["current_room"] == "Grand Hall":
            print("你使用钥匙打开了锁着的门。")
            rooms["Grand Hall"]["exits"]["east"] = "Secret Room"  # 解锁新房间
        else:
            print("你使用了:", item)
    else:
        print("你没有", item)

# 主游戏循环
def game_loop():
    print("欢迎来到古堡探险游戏！")
    look()

    while True:
        command = input("请输入指令: ").strip().lower().split()
        if not command:
            continue

        action = command[0]
        if action == "look":
            look()
        elif action == "go":
            if len(command) > 1:
                go(command[1])
            else:
                print("请指定方向。")
        elif action == "take":
            if len(command) > 1:
                take(command[1])
            else:
                print("请指定物品。")
        elif action == "inventory":
            inventory()
        elif action == "use":
            if len(command) > 1:
                use(command[1])
            else:
                print("请指定物品。")
        elif action == "quit":
            print("游戏结束。")
            break
        else:
            print("未知指令。")

# 运行游戏
game_loop()