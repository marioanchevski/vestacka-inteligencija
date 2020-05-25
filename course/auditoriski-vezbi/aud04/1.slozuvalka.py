from searching_framework.utils import Problem
from searching_framework.informed_search import greedy_best_first_graph_search, astar_search, \
    recursive_best_first_search

class Puzzle(Problem):
    def __init__(self,initial,goal):
        super().__init__(initial,goal)

    def successor(self, state):
        """
        '*32415678'
        0 1 2
        3 4 5
        6 7 8
        """
        successors = dict()
        index = state.index('*')

        if index >= 3:
            tmp = list(state)
            tmp[index], tmp[index-3] = tmp[index-3],tmp[index]
            new_state = ''.join(tmp)
            successors['Gore']=new_state
        if index <= 5:
            tmp = list(state)
            tmp[index], tmp[index+3] = tmp[index+3],tmp[index]
            new_state = ''.join(tmp)
            successors['Dolu']=new_state
        if index%3 != 0:
            tmp = list(state)
            tmp[index], tmp[index-1] = tmp[index-1],tmp[index]
            new_state = ''.join(tmp)
            successors['Levo']=new_state
        if index%3 != 2:
            tmp = list(state)
            tmp[index], tmp[index+1] = tmp[index+1],tmp[index]
            new_state = ''.join(tmp)
            successors['Desno']=new_state


        return successors

    def h(self,node):
        """
        funckojata zip
        [1, 2, 3] ['a', 'b', 'c']
        [(1,'a'), (2,'b'), (3,'c')]
        """
        counter = 0
        for x,y in zip(node.state, self.goal):
            if x!=y:
                counter += 1

        return counter

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

class Puzzle_2(Puzzle):
    coords = {0: (0, 2), 1: (1, 2), 2: (2, 2), 3: (0, 1),
              4: (1, 1), 5: (2, 1), 6: (0, 0), 7: (1, 0), 8: (2, 0)}

    @staticmethod
    def mhd(n, m):
        x1, y1 = Puzzle_2.coords[n]
        x2, y2 = Puzzle_2.coords[m]
        return abs(x1 - x2) + abs(y1 - y2)

    def h(self,node):
        sum_value = 0
        for x in '12345678':
            val = Puzzle_2.mhd(node.state.index(x), int(x))
            sum_value += val
        return sum_value


puzzle = Puzzle('*32415678', '*12345678')
result1 = greedy_best_first_graph_search(puzzle)
print(result1.solution())
result2 = astar_search(puzzle)
print(result2.solution())
result3 = recursive_best_first_search(puzzle)
print(result3.solution())


puzzle = Puzzle_2('*32415678', '*12345678')
result1 = greedy_best_first_graph_search(puzzle)
print(result1.solution())
result2 = astar_search(puzzle)
print(result2.solution())
result3 = recursive_best_first_search(puzzle)
print(result3.solution())
