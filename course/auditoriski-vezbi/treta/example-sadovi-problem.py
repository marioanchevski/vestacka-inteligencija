from utils import Problem
from uninformed_search import *


class Example(Problem):
    def __init__(self,capacitet,initial,goal):
        super().__init__(initial,goal)
        self.capacitet=capacitet

    def successor(self, state):
        successors = dict()
        j0, j1 = state
        c0, c1 = self.capacitet

        if j0 > 0:
            successors['Isprazni go sadot J0'] = (0,j1)
        if j1 > 0:
            successors['Isprazni go sadot J1'] = (j0,0)
        if j0 > 0 and j1 < c1:
            razlika = min(c1-j1,j0)
            successors['Preturi od J0 vo J1']=(j0 - razlika,j1 + razlika)
        if j1 > 0 and j0 < c0:
            razlika=min(c0-j0,j1)
            successors['Preturi od J1 vo J0']=(j0 + razlika,j1 - razlika)

        return successors


    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]


    def goal_test(self, state):
        return state == self.goal

if __name__=="__main__":

    test1 = Example([30,30],(10,5),(0,15))

    result = breadth_first_graph_search(test1)
    print(result.solution())
    print(result.solve())

    result = depth_first_graph_search(test1)
    print(result.solution())
    print(result.solve())