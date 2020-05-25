from searching_framework.utils import Problem
from searching_framework.uninformed_search import *

def update_obsticle1(position):
    x = position[0]
    y = position[1]
    nasoka = position[2]

    if x == 5 or x == 0:
        nasoka *= -1
        x = x - nasoka

    x_new = x - nasoka
    new_position = x_new, y, nasoka
    return new_position


def update_obsticle2(position):
    x = position[0]
    y = position[1]
    nasoka = position[2]

    if (x == 5 and y == 5) or (x == 0 and y == 0):
        nasoka *= -1
        x = x + nasoka
        y = y + nasoka
    x_new = x + nasoka
    y_new = y + nasoka
    new_position = x_new, y_new, nasoka
    return new_position


def update_obsticle3(position):
    x = position[0]
    y = position[1]
    nasoka = position[2]

    if y == 5 or y == 0:
        nasoka *= -1
        y = y + nasoka
    y_new = y + nasoka

    new_position = x, y_new, nasoka
    return new_position


def is_ok(x, y, p1, p2, p3):
    if x < 0 or y < 0 or x > 10 or y > 10:
        return False
    if x > 5 and y > 5:
        return False

    if (x == p1[0] and y == p1[1]) or (x == p1[0] + p1[2] and y == p1[1]):
        return False
    if (x == p2[0] and y == p2[1]) or (x == p2[0] - p2[2] and y == p2[1]) or (x == p2[0] and y == p2[1] - p2[2]) or (
            x == p2[0] - p2[2] and y == p2[1] - p2[2]):
        return False
    if (x == p3[0] and y == p3[1]) or (x == p3[0] and y == p3[1] - p3[2]):
        return False

    return True


class Prepreki(Problem):
    def __init__(self, initial, goal):
        super().__init__(initial, goal)

    def successor(self, state):
        successors = dict()
        # pozicija na coveche
        player_x = state[0]
        player_y = state[1]

        o1 = state[2]
        o2 = state[3]
        o3 = state[4]

        o1_new = update_obsticle1(o1)
        o2_new = update_obsticle2(o2)
        o3_new = update_obsticle3(o3)

        # desno
        new_x = player_x + 1
        if is_ok(new_x, player_y, o1_new, o2_new, o3_new):
            successors["Desno"] = (new_x, player_y, o1_new, o2_new, o3_new)

        # levo
        new_x = player_x - 1
        if is_ok(new_x, player_y, o1_new, o2_new, o3_new):
            successors["Levo"] = (new_x, player_y, o1_new, o2_new, o3_new)

        # gore
        new_y = player_y + 1
        if is_ok(player_x, new_y, o1_new, o2_new, o3_new):
            successors["Gore"] = (player_x, new_y, o1_new, o2_new, o3_new)

        # dole
        new_y = player_y - 1
        if is_ok(player_x, new_y, o1_new, o2_new, o3_new):
            successors["Dolu"] = (player_x, new_y, o1_new, o2_new, o3_new)

        return successors

    def actions(self, state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        position = [state[0], state[1]]
        return position == self.goal


if __name__ == '__main__':
    # Vcituvanje na vleznite argumenti za test primerite
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())
    obsticles = ((2, 8, 1), (3, 3, 1), (8, 2, -1))

    pocetna = (man_x, man_y, obsticles[0], obsticles[1], obsticles[2])
    goal = [house_x, house_y]

    covece1 = Prepreki(pocetna, goal)
    result = breadth_first_graph_search(covece1)
    print(result.solution())