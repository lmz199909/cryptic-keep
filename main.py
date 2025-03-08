#引入.py文件
from help import helps
#房间初始状态 东西南北=east,west,south,north
rooms={
    "Foyer":{
    "description":"""你身处古堡的阴暗⻔厅。头顶⼀盏布满蜘蛛⽹的吊灯微微摇晃，投下忽明忽暗的光芒。
空⽓中弥漫着潮湿的霉味，脚下是冰冷的⼤理⽯地⾯。北⾯是⼀扇沉重的橡⽊⻔，
⻔上雕刻着狰狞的怪兽头像，东⾯则是⼀条通向⿊暗深处的⾛廊。""",
    "things":{"门厅地毯下的纸条":"⼀张陈旧的纸条，似乎是从某本书⻚上撕下来的，上⾯潦草地写着 ‘光芒指引⽅向’。"},
    "way":{"north":"Grand Hall","east":"Hallway"}
    },
    "Grand Hall":{
    "description":"""你推开橡⽊⻔，进⼊了古堡的宏伟的⼤厅。尽管岁⽉流逝，依稀可⻅昔⽇的辉煌,
⼀个巨⼤的⽔晶吊灯（虽然已经缺了⼏盏灯泡）仍然悬挂在⾼耸的天花板上。彩⾊玻璃窗阻挡了外
界的光线，使得⼤厅内光线昏暗。南⾯是你进来的⻔厅，⻄⾯是⼀扇装饰华丽的⽊⻔，通往图书馆，
东⾯则是⼀道拱形⽯⻔，通向餐厅。""",
    "things":{"壁炉拨⽕棍":"⼀根沉重的铁制拨⽕棍，顶端装饰着狮⼦头。"},
    "way":{"south":"Foyer","west":"Library","east":"Dining Room"}
    },
    "Hallway":{
    "description":"""你沿着昏暗的⾛廊前⾏，脚踩在吱吱作响的⽊地板上。墙壁上挂着褪⾊的家族画像，
画像中的⼈物表情模糊不清，仿佛在注视着你。⾛廊尽头似乎传来微弱的滴⽔声。⻄⾯是⻔厅。""",
    "things":{"⽣锈的铁钥匙":"⼀把锈迹斑斑的铁钥匙，看起来年代久远，也许能打开古堡的某扇⻔。"},
    "way":{"west":"Foyer"}
    },
    "Library":{
    "description":"""你推开装饰华丽的⽊⻔，⾛进了布满灰尘的图书馆。⾼耸的书架⼀直延伸到天花板，上
⾯堆满了布满灰尘的书籍。空⽓中弥漫着浓重的旧书和⽪⾰的味道，令⼈昏昏欲睡。阳光透过
⾼窗洒进来，照亮了书架上零星散落的⾦箔。东⾯是通往⼤厅的⽊⻔。""",
"things":{"""⼀本厚重的古书":"⼀本⽪⾯精装的古书，书⻚已经泛⻩，封⾯上⽤难以辨认的⽂字
写着书名。翻开书⻚，⾥⾯似乎是关于古堡历史的记载。"""},
    "way":{"east":"Grand Hall"}
    },
    "Dining Room":{
    "description":"""你穿过拱形⽯⻔，来到了宽敞的餐厅。⻓⻓的橡⽊餐桌上布满了厚厚的灰尘，锈迹斑斑
的银质餐具散落在桌⾯上，仿佛⼀场盛宴突然中断。墙壁上挂着巨⼤的狩猎场景油画，画布已
经开始剥落。⻄⾯是通往⼤厅的拱形⽯⻔，北⾯是⼀扇破旧的⽊⻔，通向厨房。""",
    "things":{"餐桌上的银⾊烛台":"⼀个精致的银⾊烛台，上⾯镶嵌着⼀些宝⽯，但⼤部分已经脱落。"},
    "way":{"west":"Grand Hall","north":"Kitchen"}
    },
    "Kitchen":{
    "description":"""你推开破旧的⽊⻔，进⼊了阴冷潮湿的厨房。腐烂的⽓味扑⿐⽽来，令⼈作呕。⽣锈的
厨具散落在各处，巨⼤的壁炉已经冰冷，炉膛⾥堆满了⿊⾊的灰烬。南⾯是餐厅。地板中央，
你注意到⼀块不寻常的⽊板，似乎可以移动，也许是⼀个隐蔽的活板⻔，通往地下。""",
    "things":{"壁炉旁的⽕柴":"⼀盒潮湿的⽕柴，看起来还能⽤，也许可以点燃什么。⽔槽边的⽔桶:⼀个破旧的⽊⽔桶，⾥⾯积满了浑浊的⾬⽔。"},
    "way":{"south":"Dining Room","down":"Outway"}
    },
    "Outway":{
    "description":"""你打开了隐蔽的活板门，顺着梯子爬了下去。眼前是一条黑暗的地下通道，通道尽头隐约可见一丝光亮。
你朝着光亮走去，终于找到了出口，成功逃离了古堡！"""}
}

#初始化player
player={"now_room":"Foyer",
        "bag":{}}

#player move
def move_player(direction):
    time_room=rooms[player["now_room"]]
    if direction in time_room["way"]:
       player["now_room"]=time_room["way"][direction]
       print(rooms[player["now_room"]]["description"])
       if direction=="down":
           return True   
    else:
        print("没有路")
    return False
 
#player拾取装备
def take_item(it):
    time_room=rooms[player["now_room"]]
    if it in time_room["things"]:
        player["bag"][it]=time_room["things"][it]
        del time_room["things"][it]
        print(f"你拾取了{it}")
    else:
        print("没有目标")

#查看背包
def inventory():
    if player["bag"]:
        print("你的背包里有：")
        for it,describtion in player["bag"].items():
            print(f"{it}:{describtion}")
    else:
        print("你的背包空空如也")
        
#查看环境
def look():
    time_room=rooms[player["now_room"]]
    print(time_room["description"])
    #if time_room["way"]:
    #    for a,b in time_room["way"].items():
    #       print(f"{a}:{b}")
    if time_room["things"]:
        print("房间内物品：")
        for it,describtion in time_room["things"].items():
            print(f"{it}:{describtion}")
    else:
        print("房间内没有物品")
    #print("可通往的方向: "+",".join(time_room["way"].keys()))没有后续房间名称
    print("可通往的方向：")
    for way,room in time_room["way"].items():
        print(f"{way}:{room}")

#游戏开始
input("Enter键开始")
print("你是⼀名冒险家，迷失在森林中，偶然发现了⼀座神秘的古堡。",end="")
print("为了躲避⻛⾬，你推开了古堡虚掩的⼤⻔。现在你身处古堡之中，需要找到出⼝，安全逃离。")
input("Enter键继续")
print("你身处古堡的阴暗⻔厅。头顶⼀盏布满蜘蛛⽹的吊灯微微摇晃，投下忽明忽暗的光芒。",end="")
print("空⽓中弥漫着潮湿的霉味，脚下是冰冷的⼤理⽯地⾯。北⾯是⼀扇沉重的橡⽊⻔，⻔上雕刻着",end="") 
print("狰狞的怪兽头像，东⾯则是⼀条通向⿊暗深处的⾛廊。")

#game main loop
while True:
    s=input("<").strip().lower()
    if s=="help":
        helps()
    elif s.startswith("go"):
        s=s.split(" ")[1]
        game_over=move_player(s)
        if game_over:
            print("恭喜通关！")
            break
    elif s.startswith("take"):
        s=s.split(" ")[1]
        take_item(s)
    elif s=="look":
        look()
    elif s=="inventory":
        inventory()
    elif s=="quit" or s== "exit":
        break
    else:
        print("未知指令")
        continue