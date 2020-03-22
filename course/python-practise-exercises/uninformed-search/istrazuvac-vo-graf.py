from utils import Problem
from uninformed_search import *

def move_right(pos,vrski):
    if (pos,pos+1) in vrski:
        pos=pos+1
    return pos
def move_left(pos,vrski):
    if (pos,pos-1) in vrski:
        pos=pos-1
    return pos
def move_up(pos,vrski):
    if (pos,pos-4) in vrski:
        pos=pos-4
    return pos
def move_down(pos,vrski):
    if (pos,pos+4) in vrski:
        pos=pos+4
    return pos

def move_down_right(pos,vrski):
    if(pos,pos+5) in vrski:
        pos=pos+5
    return pos
def move_up_left(pos,vrski):
    if(pos,pos-5) in vrski:
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
        vrski=self.vrski


        new_pos=move_right(cur_pos,vrski)
        if new_pos != cur_pos:
            vrski.remove((new_pos, cur_pos))
            vrski.remove((cur_pos, new_pos))
            cur_pos=new_pos
            successors["Desno"]=(new_pos, tuple([s for s in dzvezdi if s != new_pos ]))
            #print(" successors[Desno]= "+str((new_pos, tuple([s for s in dzvezdi if s != new_pos ]))))


        new_pos=move_left(cur_pos,vrski)
        if new_pos != cur_pos:
            vrski.remove((new_pos, cur_pos))
            vrski.remove((cur_pos, new_pos))
            cur_pos = new_pos
            successors["Levo"] = (new_pos, tuple([s for s in dzvezdi if s != new_pos]))
            #print(" successors[levo]= "+str((new_pos, tuple([s for s in dzvezdi if s != new_pos ]))))

        new_pos = move_up(cur_pos, vrski)
        if new_pos != cur_pos:
            vrski.remove((new_pos, cur_pos))
            vrski.remove((cur_pos, new_pos))
            cur_pos = new_pos
            #print(" successors[gore]= " + str((new_pos, tuple([s for s in dzvezdi if s != new_pos ]))))


        new_pos = move_down(cur_pos, vrski)
        if new_pos != cur_pos:
            vrski.remove((new_pos, cur_pos))
            vrski.remove((cur_pos, new_pos))
            cur_pos = new_pos
            #print(" successors[Dolu]= "+str((new_pos, tuple([s for s in dzvezdi if s != new_pos ]))))


        new_pos = move_up_left(cur_pos, vrski)
        if new_pos != cur_pos:
            vrski.remove((new_pos, cur_pos))
            vrski.remove((cur_pos, new_pos))
            cur_pos = new_pos
            #print(" successors[gorelevo]= "+str((new_pos, tuple([s for s in dzvezdi if s != new_pos ]))))


        new_pos = move_down_right(cur_pos, vrski)
        if new_pos != cur_pos:
            vrski.remove((new_pos, cur_pos))
            vrski.remove((cur_pos, new_pos))
            cur_pos=new_pos
            #print(" successors[doluDesno]= "+str((new_pos, tuple([s for s in dzvezdi if s != new_pos ]))))

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        #print(self.goal)
        return len(state[-1]) == 0

if __name__=="__main__":
    #player_position = int(input())
    #star_one_position = int(input())
    #star_two_position = int(input())

    #sostojba =(player_position,(star_one_position,star_two_position))
    istrazuvac1=Istrazuvac((6,(1,16)))
    answer = breadth_first_graph_search(istrazuvac1)
    print(answer.solution())
