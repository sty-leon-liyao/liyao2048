

class GameConsolView:
    def __init__(self):
        self.__controller=GameCoreController()

    def start(self):
        self.__controller.generater_new_number()
        self.__controller.generater_new_number()
        self.__print_map()

    def __print_map(self):
        os.system("clear")
        for r in range(len(self.__controller.map)-1):
            for c in range(len(self.__controller.map[r])-1):
                print(self.__controller.map[r][c],end="\t")
            print()

    def update(self):
        while True:
            self.__controller.__move_map()
            if self.__controller.is_change:
                #如果地图发生变化
                self.__controller.generater_new_number()
                #产生一个新的数
                self.__print_map()#打印出来
                if self.__controller.is_game_over():
                    #打印出来后看游戏是否结束
                    print("游戏结束！")
                    break

    def __move_map(self):
        dir=input("请输入移动方向（wsad）：")
        if dir=="w":
            self.__controller.move(Dirction.up)
        elif dir=="s":
            self.__controller.move(Direction.down)
        elif dir=="a":
            self.__controller.move(Direction.left)
        elif dir=="d":
            self.__controller.move(Direction.right)

class GameCoreController:
    def __init__(self):
        pass
    def generater_new_number(self):
        self.__caculate_empty_location()
        if len(self.__list_empty_location)==0
            return
        loc=random.choice(self.__list_empty_location)


    def move(self):

    def is_game_over(self):







