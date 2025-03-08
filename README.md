# 游戏代码说明
## 房间初始化`rooms`
使用字典的嵌套，在玩家进行输入指令时，（根据获取的键）调用键值，输出房间的信息。
## 玩家信息初始化`player`
`now_room`首先用来初始化角色所处位置，之后用`move_player`修改键值，用来记录角色位置，调用`rooms`的键值。
`bag`设置空字典，初始化背包为空，之后可根据`take_item`将`rooms`中的`tjings`传入，在调用`inventory`打印出来。
## help模块
`from help import helps`引入函数，`or help in range(len(helps_list)):`循环打印。
## 玩家移动模块
`time_room`获取玩家当前位置，方便后续代码书写，`if direction in time_room["way"]:`通过字典内的值，判断方向是否可行，并防止玩家直接输入`down`直接通关，若是可行，更新玩家位置并打印新房间描述，若不可行，打印没有路。
## 拾取装备模块`take_item`
首先获取玩家位置，方便后续代码书写`time_room=rooms[player["now_room"]]`，查找字典内是否有对应物品，若是有，则在`bag`中创建一个新的键值对`player["bag"][it]`,然后通过赋值语句添加。防止玩家可重复拾取物品和`look`指令可查看到已被拾取的物品，通过`del`删除字典中的内容。若是没有对应物品则输出：没有目标，提示玩家。
## 查看背包模块
通过`if`判断背包内是否有物品，若是没有，输出你的背包空空如也，若是有，可能则通过循环打印bag中的物品。
## 查看环境模块
`time_room`获取当前角色所处位置，简化后续代码，`print(time_room["description"]`打印出所处房间描述，`if time_room["things"]:`判断房间内是否有物品，防止物品被玩家拾取后，`look`指令依旧打印`房间内物品：`，通过循环和`items`打印输出。
## 游戏开始模块
用`input`特性实现`enter`继续。
## 游戏主循环模块
使用`while`循环，不断处理玩家指令，`s=input("<").strip().lower()`获取玩家指令，将输入改为小写和去除两边空格，增加用户容错性，使用`if`对输入的指令进行分流，使用`split`对输入的指令进行切割，获取程序所需要的部分。