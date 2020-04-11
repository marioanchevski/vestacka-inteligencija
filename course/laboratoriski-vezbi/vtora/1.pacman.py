from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Pacman(Problem):
    def __init__(self,initial,goal=None):
        super().__init__(initial,goal)
        self.precki = [(0,6),(0,8),(0,9),(1,2),(1,3),(1,4),
                       (1,9),(2,9),(3,6),(3,9),(4,1),(4,5),
                       (4,6),(4,7),(5,1),(5,6),(6,0),(6,1),
                       (6,2),(6,9),(8,1),(8,4),(8,7),(8,8),
                       (9,4),(9,7),(9,8)]

    def successor(self, state):
        successors = dict()
        x=state[0]
        y=state[1]
        pravec=state[2]
        tocki=state[3]

        #prodolzhi pravo
        if pravec=='istok' and ((x+1,y)  not in self.precki and x+1<=9):
            successors['ProdolzhiPravo']=(x+1,y,'istok',tuple([t for t in tocki if t != (x+1,y)]))
        elif pravec=='zapad'and ((x-1,y)  not in self.precki and x-1>=0):
            successors['ProdolzhiPravo'] = (x - 1, y, 'zapad', tuple([t for t in tocki if t != (x - 1, y)]))
        elif pravec=='sever' and ((x,y+1) not in self.precki and y+1<=9):
            successors['ProdolzhiPravo'] = (x, y+1, 'sever', tuple([t for t in tocki if t != (x, y+1)]))
        elif pravec == 'jug' and ((x, y - 1) not in self.precki and y - 1 >= 0):
            successors['ProdolzhiPravo'] = (x, y-1, 'jug', tuple([t for t in tocki if t != (x, y-1)]))

        #prodolzhi nazad
        if pravec=='istok' and ((x-1,y) not in self.precki and x-1>=0):
            successors['ProdolzhiNazad']=(x-1,y,'zapad',tuple([t for t in tocki if t != (x - 1, y)]))
        elif pravec=='zapad' and ((x+1,y) not in self.precki and x+1<=9):
            successors['ProdolzhiNazad'] = (x + 1, y, 'istok', tuple([t for t in tocki if t != (x + 1, y)]))
        elif pravec=='sever' and ((x,y-1) not in self.precki and y-1>=0):
            successors['ProdolzhiNazad'] = (x, y-1, 'jug', tuple([t for t in tocki if t != (x, y-1)]))
        elif pravec=='jug' and ((x,y+1) not in self.precki and y+1<=9):
            successors['ProdolzhiNazad'] = (x, y + 1, 'sever', tuple([t for t in tocki if t != (x, y + 1)]))

        #svrti levo
        if pravec=='istok' and ((x,y+1) not in self.precki and y+1<=9):
            successors['SvrtiLevo'] = (x, y + 1, 'sever', tuple([t for t in tocki if t != (x, y + 1)]))
        elif pravec=='zapad' and ((x,y-1) not in self.precki and y-1>=0):
            successors['SvrtiLevo'] = (x, y - 1, 'jug', tuple([t for t in tocki if t != (x, y - 1)]))
        elif pravec=='sever' and ((x-1,y) not in self.precki and x-1>=0):
            successors['SvrtiLevo'] = (x-1, y, 'zapad', tuple([t for t in tocki if t != (x-1, y)]))
        elif pravec=='jug' and ((x+1,y) not in self.precki and x+1<=9):
            successors['SvrtiLevo'] = (x + 1, y, 'istok', tuple([t for t in tocki if t != (x + 1, y)]))

        #svrti desno
        if pravec=='istok' and ((x,y-1) not in self.precki and y-1>=0):
            successors['SvrtiDesno']=(x,y-1,'jug',tuple([t for t in tocki if t != (x, y - 1)]))
        elif pravec=='zapad' and ((x,y+1) not in self.precki and y+1<=9):
            successors['SvrtiDesno'] = (x, y + 1, 'sever', tuple([t for t in tocki if t != (x, y + 1)]))
        elif pravec=='sever' and ((x+1,y) not in self.precki and x+1<=9):
            successors['SvrtiDesno'] = (x+1, y, 'istok', tuple([t for t in tocki if t != (x+1, y)]))
        elif pravec=='jug' and ((x-1,y) not in self.precki and x-1>=0):
            successors['SvrtiDesno'] = (x - 1, y, 'zapad', tuple([t for t in tocki if t != (x - 1, y)]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[-1])==0


if __name__=="__main__":

    tocki = []
    pacman_x = int(input())
    pacman_y = int(input())
    nasoka = input()
    n = int(input())
    for i in range(n):
        coords = input().split(",")
        tocki.append((int(coords[0]),int(coords[1])))
    tocki = tuple(tocki)

    pocetna_sostojba = (pacman_x,pacman_y,nasoka,tocki)
    pacman = Pacman(pocetna_sostojba)
    solution = breadth_first_graph_search(pacman)
    print(solution.solution())