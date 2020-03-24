from utils import Problem
from uninformed_search import *


def move_right(pos,vrski):
    if (pos,pos+1) in vrski:
        vrski.remove((pos, pos+1))
        vrski.remove((pos+1, pos))
        pos=pos+1
    return pos
def move_left(pos,vrski):
    if (pos,pos-1) in vrski:
        vrski.remove((pos, pos-1))
        vrski.remove((pos-1, pos))
        pos=pos-1
    return pos
def move_up(pos,vrski):
    if (pos,pos-4) in vrski:
        vrski.remove((pos,pos-4))
        vrski.remove((pos-4, pos))
        pos=pos-4
    return pos
def move_down(pos,vrski):
    if (pos,pos+4) in vrski:
        vrski.remove((pos, pos+4))
        vrski.remove((pos+4,pos))
        pos=pos+4
    return pos

def move_down_right(pos,vrski):
    if(pos,pos+5) in vrski:
        vrski.remove((pos,pos+5))
        vrski.remove((pos+5, pos))
        pos=pos+5
    return pos
def move_up_left(pos,vrski):
    if(pos,pos-5) in vrski:
        vrski.remove((pos, pos-5))
        vrski.remove((pos-5,pos))
        pos=pos-5
    return pos

class Istrazuvac(Problem):
    def __init__(self,initial,goal=None):
        super().__init__(initial,goal)
        self.vrski=[(1, 2), (1, 5), (2, 6), (5, 6), (3, 7), (3, 4), (4, 8),
            (7, 8), (9, 10), (9, 13), (10, 14), (13, 14), (11, 12),
            (11, 15), (12, 16), (15, 16), (6, 7), (6, 10),(6,11),(11,6),
            (10, 11), (7, 11), (2, 1), (5, 1), (6, 2), (6, 5), (7, 3),
            (4, 3), (8, 4), (8, 7), (10, 9), (13, 9), (14, 10), (14, 13),
            (12, 11), (15, 11), (16, 12), (16, 15), (7, 6), (10, 6), (11, 10), (11, 7)]


    def successor(self, state):
        successors = dict()
        cur_pos = state[0]
        dzvezdi = state[1]

        new_position=move_right(cur_pos,self.vrski)
        if new_position != cur_pos:
            successors["Desno"]=(new_position, tuple([s for s in dzvezdi if s != new_position]))

        new_position=move_left(cur_pos,self.vrski)
        if new_position != cur_pos:
            successors["Levo"] = (new_position, tuple([s for s in dzvezdi if s != new_position]))

        new_position = move_up(cur_pos, self.vrski)
        if new_position != cur_pos:
            successors["Gore"] = (new_position, tuple([s for s in dzvezdi if s != new_position]))

        new_position = move_down(cur_pos, self.vrski)
        if new_position != cur_pos:
            successors["Dolu"] = (new_position, tuple([s for s in dzvezdi if s != new_position]))

        new_position = move_up_left(cur_pos, self.vrski)
        if new_position != cur_pos:
            successors["GoreLevo"] = (new_position, tuple([s for s in dzvezdi if s != new_position]))

        new_position= move_down_right(cur_pos, self.vrski)
        if new_position != cur_pos:
            successors["DoluDesno"] = (new_position, tuple([s for s in dzvezdi if s != new_position]))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return len(state[1]) == 0

if __name__=="__main__":
    #player_position = int(input())
    #star_one_position = int(input())
    #star_two_position = int(input())

    #sostojba =(player_position,(star_one_position,star_two_position))
    istrazuvac1=Istrazuvac((6,(1,16)))
    answer = breadth_first_graph_search(istrazuvac1)
    print(answer.solution())
