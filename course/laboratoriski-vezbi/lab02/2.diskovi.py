from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

class Diskovi(Problem):
    def __init__(self,initial,goal):
        super().__init__(initial,goal)

    def successor(self, state):
        successors = dict()
        lista = list(state)

        for i in range(len(lista)):
            lista = list(state)
            if lista[i]!="#":
                if i+1<len(lista) and lista[i+1]=="#":
                    st = "D1: Disk " + str(lista[i])
                    lista[i+1]=lista[i]
                    lista[i]="#"
                    successors[st]=tuple(lista)
                    lista=list(state)
                if i+2<len(lista) and lista[i+2]=="#" and lista[i+1]!="#":
                    st = "D2: Disk " + str(lista[i])
                    lista[i + 2] = lista[i]
                    lista[i] = "#"
                    successors[st] = tuple(lista)
                    lista = list(state)
                if i-1>=0 and lista[i-1]=="#":
                    st = "L1: Disk " + str(lista[i])
                    lista[i - 1] = lista[i]
                    lista[i] = "#"
                    successors[st] = tuple(lista)
                    lista = list(state)
                if i-2>=0 and lista[i-2]=="#" and lista[i-1]!="#":
                    st = "L2: Disk "+str(lista[i])
                    lista[i-2]=lista[i]
                    lista[i]="#"
                    successors[st]=tuple(lista)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state == self.goal


if __name__ == '__main__':
    n = int(input())
    l = int(input())
    lista=[]
    for i in range(n):
        lista.append(i+1)
    for i in range(l-n):
        lista.append("#")

    cel = lista[:]
    cel.reverse()

    lista=tuple(lista)
    cel=tuple(cel)


    disk_problem = Diskovi(lista,cel)
    answer = breadth_first_graph_search(disk_problem)
    print(answer.solution())