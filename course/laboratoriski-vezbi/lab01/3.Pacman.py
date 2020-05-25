import random

class Player:
    def __init__(self,position):
        self.x=position[0]
        self.y=position[1]

    def move(self,position):
        self.position=position
        print(position)

class Game:
    def __init__(self,map,size_x,size_y):
        self.map=map
        self.size_x=size_x
        self.size_y=size_y

class Pacman:
    def __init__(self,map):
        self.player = Player([0,0])
        self.game = Game(map[0],map[1],map[2])

    def food_left(self):
        for i in range(self.game.size_x):
            for j in range(self.game.size_y):
                if self.game.map[i][j]=='.':
                    return True
        return False


    def play_game(self):

        cur_x=self.player.x
        cur_y=self.player.y
        map_has_dots=False

        while(self.food_left()):
            map_has_dots=True
            next_move = []  # list of next possible move ['value',[x,y]]
            #down
            if cur_x+1<self.game.size_x:
                next_move.append([self.game.map[cur_x+1][cur_y],[cur_x+1,cur_y]])
            #up
            if cur_x-1>=0:
                next_move.append([self.game.map[cur_x-1][cur_y],[cur_x-1,cur_y]])
            #right
            if cur_y+1<self.game.size_y:
                next_move.append([self.game.map[cur_x][cur_y+1],[cur_x,cur_y+1]])
            #left
            if cur_y-1>=0:
                next_move.append([self.game.map[cur_x][cur_y-1],[cur_x,cur_y-1]])

            #broj na posakuvani cekori
            num_dot=0
            for i in range(len(next_move)):
                if next_move[i][0]==".":
                    num_dot += 1

            if num_dot==1:
                for i in range(len(next_move)):
                    if next_move[i][0] == ".":
                        cur_x=next_move[i][1][0]
                        cur_y=next_move[i][1][1]
                        self.player.move([cur_x,cur_y])
                        self.game.map[cur_x][cur_y]="#"
                        break
            elif num_dot>1:
                # p --> lista od site posakuvani potezi (kade vrednosta e '.')
                p=[elem for elem in next_move if elem[0]=='.']
                random_move=random.randint(0,len(p)-1)
                cur_x = p[random_move][1][0]
                cur_y = p[random_move][1][1]
                self.player.move([cur_x, cur_y])
                self.game.map[cur_x][cur_y] = "#"
            else:
                random_move=random.randint(0,len(next_move)-1)
                cur_x = next_move[random_move][1][0]
                cur_y = next_move[random_move][1][1]
                self.player.move([cur_x, cur_y])
                self.game.map[cur_x][cur_y] = "#"

        if map_has_dots==False:
            print("Nothing to do here")


def create_map():
    visina = int(input())
    sirina = int(input())
    row = []
    map = []
    for i in range(visina):
        string = input()
        for j in range(sirina):
            row.append(string[j])
        map.append(row)
        row = []
    return [map,visina,sirina]

if __name__=="__main__":
    pacman =  Pacman(create_map())
    pacman.play_game()

