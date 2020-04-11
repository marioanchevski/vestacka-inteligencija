from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Explorer(Problem):

    def __init__(self,initial,goal):
        super().__init__(initial,goal)
        self.map_size=[8,6]

    def successor(self, state):
        successors = dict()
        # x and y positions of player
        x = state[0]
        y = state[1]

        #map size
        max_x = self.map_size[0]
        max_y = self.map_size[1]

        #obsticles [ x, y, direction ]
        # direction: -1 = up 1 = down
        p1 = [state[2], state[3], state[4]]
        p2 = [state[5], state[6], state[7]]


        def pridvizi_prepreka(prepreka):
            y = prepreka[1]
            nasoka = prepreka[2]

            if nasoka == 1:
                y -= 1
            else:
                y += 1

            if y == 0 or y == 7:
                nasoka = nasoka * -1
            prepreka = [prepreka[0], y, nasoka]
            return prepreka

        p1 = pridvizi_prepreka(p1)
        p2 = pridvizi_prepreka(p2)
        prepreki = [[p1[0],p1[1]],[p2[0],p2[1]]]

        if x<max_x-1 and [x+1,y] not in prepreki :
            successors['Desno']=(x+1,y,
                                 p1[0],p1[1],p1[2],
                                 p2[0],p2[1],p2[2])
        if x>0 and [x-1,y] not in prepreki:
            successors['Levo'] = (x-1, y,
                                 p1[0],p1[1],p1[2],
                                 p2[0],p2[1],p2[2])
        if y<max_y-1 and [x,y+1] not in prepreki:
            successors['Gore'] = (x,y+1,
                                 p1[0],p1[1],p1[2],
                                 p2[0],p2[1],p2[2])
        if y>0 and [x,y-1] not in prepreki:
            successors['Dolu'] = (x,y-1,
                                 p1[0],p1[1],p1[2],
                                 p2[0],p2[1],p2[2])

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = (state[0],state[1])
        return position == self.goal

if __name__=="__main__":

    cel = (7,4)
    pocetna_lokacija = (0,2)
    prepreka1 = (1,3,1)
    prepreka2 = (5,0,-1)
    explorer1 = Explorer((pocetna_lokacija[0],pocetna_lokacija[1],
                          prepreka1[0],prepreka1[1],prepreka1[2],
                          prepreka2[0],prepreka2[1],prepreka2[2]),cel)


    print(breadth_first_graph_search(explorer1).solution())
    print(breadth_first_graph_search(explorer1).solve())