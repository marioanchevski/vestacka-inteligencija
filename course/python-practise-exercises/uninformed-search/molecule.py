from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def move_right(x1,y1,x2,y2,x3,y3,obsticles):
    while x1<8 and [x1+1,y1] not in obsticles and [x1+1,y1] != [x2,y2] and [x1+1,y1] != [x3,y3]:
        x1 += 1
    return x1
def move_left(x1,y1,x2,y2,x3,y3,obsticles):
    while x1>0 and [x1-1,y1] not in obsticles and [x1-1,y1] != [x2,y2] and [x1-1,y1] != [x3,y3]:
        x1 -= 1
    return x1

def move_up(x1,y1,x2,y2,x3,y3,obsticles):
    while y1<6 and [x1,y1+1] not in obsticles and [x1,y1+1]!=[x2,y2] and [x1,y1+1]!= [x3,y3]:
        y1 += 1
    return y1
def move_down(x1,y1,x2,y2,x3,y3,obsticles):
    while y1>0 and [x1,y1-1] not in obsticles and [x1,y1-1]!=[x2,y2] and [x1,y1-1]!= [x3,y3]:
        y1 -= 1
    return y1


class Molecule(Problem):
    def __init__(self,initial,obsitcles,goal=None):
        super().__init__(initial,goal)
        self.obsitcles=obsitcles

    def successor(self, state):
        successors = dict()
        #H1
        h1_x = state[0]
        h1_y = state[1]
        #O
        o_x=state[2]
        o_y=state[3]
        #H2
        h2_x=state[4]
        h2_y=state[5]
        obsticles=self.obsitcles

        # H1
        new_y = move_up(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obsticles)
        if new_y != h1_y:
            successors['GoreH1'] = (h1_x, new_y, o_x, o_y, h2_x, h2_y)
        new_y = move_down(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obsticles)
        if new_y != h1_y:
            successors['DoluH1'] = (h1_x, new_y, o_x, o_y, h2_x, h2_y)
        new_x = move_left(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obsticles)
        if new_x != h1_x:
            successors['LevoH1'] = (new_x, h1_y, o_x, o_y, h2_x, h2_y)
        new_x = move_right(h1_x, h1_y, o_x, o_y, h2_x, h2_y, obsticles)
        if new_x != h1_x:
            successors['DesnoH1'] = (new_x, h1_y, o_x, o_y, h2_x, h2_y)

        # O
        new_y = move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obsticles)
        if new_y != o_y:
            successors['GoreO'] = (h1_x, h1_y, o_x, new_y, h2_x, h2_y)
        new_y = move_down(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obsticles)
        if new_y != o_y:
            successors['DoluO'] = (h1_x, h1_y, o_x, new_y, h2_x, h2_y)
        new_x = move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obsticles)
        if new_x != o_x:
            successors['LevoO'] = (h1_x, h1_y, new_x, o_y, h2_x, h2_y)
        new_x = move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y, obsticles)
        if new_x != o_x:
            successors['DesnoO'] = (h1_x, h1_y, new_x, o_y, h2_x, h2_y)

        # H2
        new_y = move_up(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obsticles)
        if new_y != h2_y:
            successors['GoreH2'] = (h1_x, h1_y, o_x, o_y, h2_x, new_y)
        new_y = move_down(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obsticles)
        if new_y != h2_y:
            successors['DoluH2'] = (h1_x, h1_y, o_x, o_y, h2_x, new_y)
        new_x = move_left(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obsticles)
        if new_x != h2_x:
            successors['LevoH2'] = (h1_x, h1_y, o_x, o_y, new_x, h2_y)
        new_x = move_right(h2_x, h2_y, h1_x, h1_y, o_x, o_y, obsticles)
        if new_x != h2_x:
            successors['DesnoH2'] = (h1_x, h1_y, o_x, o_y, new_x, h2_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[1]==state[3]==state[5] and state[0]+1==state[2]==state[4]-1


if __name__=="__main__":
    h1_atom_x = int(input())
    h1_atom_y = int(input())
    o_atom_x = int(input())
    o_atom_y = int(input())
    h2_atom_x = int(input())
    h2_atom_y = int(input())

    obsticles=([0,1],[1,1],[1,3],[3,1],[2,5],[3,6],[4,2],
               [6,1],[5,6],[6,2],[6,3],[7,3],[7,6],[8,5])

    initial_state=(h1_atom_x,h1_atom_y,o_atom_x,o_atom_y,h2_atom_x,h2_atom_y)
    molecule1 =  Molecule(initial_state,obsticles)
    answer = breadth_first_graph_search(molecule1)
    print(answer.solution())