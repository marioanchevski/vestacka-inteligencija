def tic_tac_toe(lista):
    if lista[0][0]==lista[0][1]==lista[0][2]:
        return lista[0][0]
    elif lista[0][0]==lista[1][0]==lista[2][0]:
        return lista[0][0]
    elif lista[0][0]==lista[1][1]==lista[2][2]:
        return lista[0][0]
    elif lista[2][0]==lista[2][1]==lista[2][2]:
        return lista[2][0]
    elif lista[0][2]==lista[1][2]==lista[2][2]:
        return lista[0][2]
    elif lista[2][0]==lista[1][1]==lista[2][0]:
        return lista[2][0]
    elif lista[1][0]==lista[1][1]==lista[1][2]:
        return lista[1][0]
    elif lista[0][1]==lista[1][1]==lista[2][1]:
        return lista[0][1]

    return "Draw"

if __name__=="__main__":
    print(tic_tac_toe([
  ["X", "X", "O"],
  ["O", "O", "X"],
  ["X", "X", "O"]
]))