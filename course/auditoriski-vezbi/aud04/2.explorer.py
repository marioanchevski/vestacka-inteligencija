from searching_framework.utils import Problem
from searching_framework.informed_search import *

def update_obsticle(obsticle):
    x, y, direction = obsticle
    if (y == 0 and direction == -1) or (y == 5 and direction == 1):
        direction *= -1
    y_new = y + direction
    new_obsticle = x, y_new, direction
    return new_obsticle


def check_collision(man , obsticle1, obsticle2):
    return man != obsticle1[:2] and man != obsticle2[:2]

class Explorer(Problem):

    def __init__(self,initial,goal):
        super().__init__(initial,goal)

    def actions(self,state):
        return self.successor(state).keys()

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        return state[0] == self.goal[0] and state[1] == self.goal[1]

    def successor(self, state):
        successors = dict()
        x = state[0]
        y = state[1]
        obsticle_1 = (state[2], state[3], state[4])
        obsticle_2 = (state[5], state[6], state[7])

        obstacle_1_new = update_obsticle(obsticle_1)
        obstacle_2_new = update_obsticle(obsticle_2)

        # Right
        if x < 7:
            x_new = x + 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Right'] = state_new

        # Left
        if x > 0:
            x_new = x - 1
            y_new = y
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Left'] = state_new

        # Up
        if y < 5:
            x_new = x
            y_new = y + 1
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Up'] = state_new

        # Down
        if y > 0:
            x_new = x
            y_new = y - 1
            man = x_new, y_new
            if check_collision(man, obstacle_1_new, obstacle_2_new):
                state_new = (x_new, y_new, obstacle_1_new[0], obstacle_1_new[1], obstacle_1_new[2],
                             obstacle_2_new[0], obstacle_2_new[1], obstacle_2_new[2])

                successors['Down'] = state_new

        return successors

    def h(self,node):
        return abs(node.state[0]-self.goal[0]) + abs(node.state[1]-self.goal[1])


if __name__ == '__main__':
    man_x = int(input())
    man_y = int(input())
    house_x = int(input())
    house_y = int(input())

    house=[house_x,house_y]
    explorer = Explorer((man_x,man_y, 2, 5, -1, 5, 0, 1), house)

    result1 = astar_search(explorer)
    print(result1.solution())