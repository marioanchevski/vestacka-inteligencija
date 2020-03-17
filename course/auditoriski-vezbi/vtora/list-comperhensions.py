#geeks-for-geeks list comprehensions excersises

def task1():
    """
    I want to create a matrix which looks like below:

matrix = [[0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4],
          [0, 1, 2, 3, 4]]
    """
    l=[[i for i in range(5)] for j in range(5)]
    print(l)


def task2():
    """
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    Expected Output: flatten_matrix = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    matrix =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    l=[elem for row in matrix for elem  in row]
    print(l)


def task3():
    """
    Suppose I want to flatten a given 2-D list and only include those strings whose lengths are less than 6:
    planets = [[‘Mercury’, ‘Venus’, ‘Earth’], [‘Mars’, ‘Jupiter’, ‘Saturn’], [‘Uranus’, ‘Neptune’, ‘Pluto’]]
    Expected Output: flatten_planets = [‘Venus’, ‘Earth’, ‘Mars’, ‘Pluto’]
    """
    planets = [['Mercury', 'Venus', 'Earth'], ['Mars', 'Jupiter', 'Saturn'], ['Uranus', 'Neptune', 'Pluto']]
    l=[elem for row in planets for elem in row if len(elem)<6]
    print(l)

if __name__=="__main__":
    task1()
    task2()
    task3()
