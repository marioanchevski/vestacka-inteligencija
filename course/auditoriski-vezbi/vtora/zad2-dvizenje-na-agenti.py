class Agent:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def dvizi(self):
        pass


    #toString metod
    def __repr__(self):
        return f'Position: ({self.x}, {self.y})'

    def kade_sum(self):
        print("x="+str(self.x)+" y="+str(self.y))


class LeftAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def dvizi(self):
        self.x-=1


class RightAgent(Agent):
    def __init__(self,x,y):
       super().__init__(x,y)

    def dvizi(self):
        self.x+=1


class UpAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def dvizi(self):
        self.y+=1


class DownAgent(Agent):
    def __init__(self,x,y):
        super().__init__(x,y)

    def dvizi(self):
        self.y-=1


if __name__=="__main__":
    left=LeftAgent(1,2)
    left.kade_sum()

    for i in range(5):
        left.dvizi()
        left.kade_sum()
        print(f'Step: {i}, {left}')
