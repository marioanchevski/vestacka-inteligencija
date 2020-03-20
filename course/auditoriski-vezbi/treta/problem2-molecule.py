from utils import Problem
from uninformed_search import *

class Molecule(Problem):

    def __init__(self,initial,goal=None):
        super().__init__(initial,goal)
        self.prepreki=[[0,1],[1,1],[1,3],[2,5],[3,1],[3,6],
                       [4,2],[5,6],[6,1],[6,2],[6,3],[7,3],
                       [7,6],[8,5]]
        #sirina 9 visina 7
        self.world_size=[8,6]


    def successor(self, state):

        successors = dict()
        #pozicii na H1
        h1_x=state[0]
        h1_y=state[1]
        #pozicii na O
        o_x=state[2]
        o_y = state[3]
        #pozicii na H2
        h2_x=state[4]
        h2_y=state[5]


        def move_right(x1,y1,x2,y2,x3,y3,prepreki):
            while x1 < self.world_size[0] and [x1+1,y1] not in self.prepreki and [x1+1,y1] != [x2,y2] and [x1+1,y1] != [x2,y2]:
                x1 += 1
            return x1

        def move_left(x1,y1,x2,y2,x3,y3,prepreki):
            while x1 > 0 and [x1-1,y1] not in self.prepreki and [x1-1,y1] != [x2,y2] and [x1-1,y1] != [x2,y2]:
                x1 -= 1
            return x1

        def move_up(x1,y1,x2,y2,x3,y3,prepreki):
            while y1 < self.world_size[1] and [x1,y1+1] not in self.prepreki and [x1,y1+1] != [x2,y2] and [x1,y1+1] != [x2,y2]:
                y1 += 1
            return y1

        def move_down(x1,y1,x2,y2,x3,y3,prepreki):
            while y1 > 0 and [x1,y1-1] not in self.prepreki and [x1,y1-1] != [x2,y2] and [x1,y1-1] != [x2,y2]:
                y1 -= 1
            return y1

        #Dvizenja za H1
        x_new =  move_right(h1_x,h1_y,o_x,o_y,h2_x,h2_y,self.prepreki)
        if x_new!=h1_x:
            successors["DesnoH1"]=(x_new,h1_y,o_x,o_y,h2_x,h2_y)

        x_new =  move_left(h1_x,h1_y,o_x,o_y,h2_x,h2_y,self.prepreki)
        if x_new!=h1_x:
            successors["LevoH1"]=(x_new,h1_y,o_x,o_y,h2_x,h2_y)
        y_new = move_up(x_new, h1_y, o_x, o_y, h2_x, h2_y,self.prepreki)
        if y_new != h1_y:
            successors["GoreH1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)
        y_new = move_down(x_new, h1_y, o_x, o_y, h2_x, h2_y,self.prepreki)
        if y_new != h1_y:
            successors["DoleH1"] = (h1_x, y_new, o_x, o_y, h2_x, h2_y)

        #Dvizenje za H2
        x_new = move_right(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.prepreki)
        if x_new != h2_x:
            successors['DesnoH2'] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)

        x_new = move_left(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.prepreki)
        if x_new != h2_x:
            successors['LevoH2'] = (h1_x, h1_y, o_x, o_y, x_new, h2_y)

        y_new = move_up(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.prepreki)
        if y_new != h2_y:
            successors['GoreH2'] = (h1_x, h1_y, o_x, o_y, h2_x, y_new)

        y_new = move_down(h2_x, h2_y, o_x, o_y, h1_x, h1_y, self.prepreki)
        if y_new != h2_y:
            successors['DoleH2'] = (h1_x, h1_y, o_x, o_y, h2_x, y_new)

        # Dvizenje za O
        x_new = move_right(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.prepreki)
        if x_new != o_x:
            successors['DesnoO'] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)

        x_new = move_left(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.prepreki)
        if x_new != o_x:
            successors['LevoO'] = (h1_x, h1_y, x_new, o_y, h2_x, h2_y)

        y_new = move_up(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.prepreki)
        if y_new != o_y:
            successors['GoreO'] = (h1_x, h1_y, o_x, y_new, h2_x, h2_y)

        y_new = move_down(o_x, o_y, h1_x, h1_y, h2_x, h2_y, self.prepreki)
        if y_new != o_y:
            successors['DoleO'] = (h1_x, h1_y, o_x, y_new, h2_x, h2_y)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):

        return state[1]==state[3]==state[5] and state[0]==state[2]-1 and state[2]+1==state[4]

if __name__ == '__main__':

    pocetna_sost =(2, 1, 7, 2, 2, 6)

    molekula1 = Molecule(pocetna_sost)
    result = breadth_first_graph_search(molekula1)
    print(result.solution())
