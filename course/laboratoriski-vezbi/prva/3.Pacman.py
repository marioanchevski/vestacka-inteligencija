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
        self.mapa=map[0]
        self.player = Player([0,0])
        self.game = Game(map[0],map[1],map[2])

    def food_left(self):

        for i in range(self.game.size_x):
            for j in range(self.game.size_y):
                if self.mapa[i][j]=='.':
                    return True
        return False

    def printi(self):
        str1 = ""
        for i in range(3):
            for j in range(3):
                str1 += self.mapa[i][j]
            str1 += "\n"
        print(str1)

        for i in range(3):
            for j in range(3):
                str1+=self.mapa[i][j]

    def play_game(self):
        next_move=[]

        cur_x=self.player.x
        cur_y=self.player.y
        position=[]
        hesoyam=0
        while(self.food_left()):
            hesoyam+=1
            #dole
            next_move=[]
            if cur_x+1<self.game.size_x:
                next_move.append([self.mapa[cur_x+1][cur_y],[cur_x+1,cur_y]])
            #nagore
            if cur_x-1>=0:
                next_move.append([self.mapa[cur_x-1][cur_y],[cur_x-1,cur_y]])
            #desno
            if cur_y+1<self.game.size_y:
                next_move.append([self.mapa[cur_x][cur_y+1],[cur_x,cur_y+1]])
            #levo
            if cur_y-1>=0:
                next_move.append([self.mapa[cur_x][cur_y-1],[cur_x,cur_y-1]])


            num_dot=0

            #print(str(next_move)+"nextt")
            for i in range(len(next_move)):
                if next_move[i][0]==".":
                    num_dot += 1

            if num_dot==1:

                for i in range(len(next_move)):
                    if next_move[i][0] == ".":
                        #self.printi()
                        #print(str(next_move) + " mozni potezi1")
                        cur_x=next_move[i][1][0]
                        cur_y=next_move[i][1][1]
                        position=[cur_x,cur_y]
                        self.player.move(position)
                        self.game.map[cur_x][cur_y]="#"
                        next_move=[]
                        break
            elif num_dot>1:
                p=[elem for elem in next_move if elem[0]=='.']
                #print(str(p)+ " elems inp")
                rand=random.randint(0,len(p)-1)
                #self.printi()
                #print(str(next_move) + " mozni potezi2")
                cur_x = p[rand][1][0]
                cur_y = p[rand][1][1]
                position = [cur_x, cur_y]
                self.player.move(position)
                self.game.map[cur_x][cur_y] = "#"
                next_move = []
                p=[]

            else:
               # self.printi()
                #print(str(next_move) + " mozni potezi3")
                rand=random.randint(0,len(next_move)-1)
                cur_x = next_move[rand][1][0]
                cur_y = next_move[rand][1][1]
                position = [cur_x, cur_y]
                self.player.move(position)
                self.game.map[cur_x][cur_y] = "#"

                next_move = []
        if hesoyam==0:
            print("Nothing to do here")





def create_map():
    n = int(input())
    m = int(input())
    row = []
    map = []
    for i in range(n):
        string = input()
        for j in range(m):
            row.append(string[j])
        map.append(row)
        row = []
    return [map,n,m]

if __name__=="__main__":
    pacman =  Pacman(create_map())
    pacman.play_game()

