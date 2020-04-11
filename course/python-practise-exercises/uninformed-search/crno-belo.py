from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def klik(x,y,lista):
    val=3
    if lista[x][y] == 0:
        val = 1
    else:
        val = 0
    for i in range(len(lista)):
        lista[x][i]=val
    for i in range(len(lista)):
        lista[i][y]=val
    return lista



class CrnoBelo(Problem):
    def __init__(self,initial,goal=None):
        super().__init__(initial,goal)


    def successor(self, state):
        successors =  dict()
        pocetna_lista=state


        # 0 0
        for i in range(len(pocetna_lista)):
            st="x: 0, y: "+str(i)
            new_state = list(map(list, pocetna_lista))
            new_state  = klik(0,i,new_state)
            new_state=tuple(map(tuple, new_state))
            successors[st]=(new_state)

        for i in range(len(pocetna_lista)):
            st=str(i)+" :0, y: 0"
            new_state = list(map(list, pocetna_lista))
            new_state  = klik(i,0,new_state)
            new_state=tuple(map(tuple, new_state))
            successors[st]=(new_state)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        for row in state:
            for column in row:
                if column == 0:
                    return False
        return True


if __name__=="__main__":
    n = int(input())

    fields = list(map(int, input().split(',')))
    p = []
    final = []
    br = 0

    for i in range(len(fields)):
        p.append(fields[i])
        br += 1
        if br % n == 0:
            final.append(p)
            p = []
            br = 0

    final = tuple(map(tuple, final))
    resenie1=CrnoBelo(final)
    answer = breadth_first_graph_search(resenie1)
    print(answer.solution())