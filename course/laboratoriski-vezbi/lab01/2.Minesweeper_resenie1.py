def resenie(lista):
    num = 0
    pom = len(lista) - 1
    for i in range(0, len(lista)):
        for j in range(0, len(lista)):
            if lista[i][j] == '-':
                if j > 0:
                    if lista[i][j - 1] == "#":
                        num = num + 1
                if j < pom:
                    if lista[i][j + 1] == "#":
                        num = num + 1
                if i > 0:
                    if lista[i - 1][j] == "#":
                        num = num + 1
                if i < pom:
                    if lista[i + 1][j] == "#":
                        num = num + 1
                if i > 0 and j > 0:
                    if lista[i - 1][j - 1] == "#":
                        num = num + 1
                if j < pom and i < pom:
                    if lista[i + 1][j + 1] == "#":
                        num = num + 1
                if i < pom and j > 0:
                    if lista[i + 1][j - 1] == "#":
                        num = num + 1
                if i > 0 and j < pom:
                    if lista[i - 1][j + 1] == "#":
                        num = num + 1
                lista[i][j] = str(num)
                num = 0

    new_str = ""
    for i in range(0, len(lista)):
        new_str = new_str + "   ".join(lista[i])
        new_str = new_str + "\n"

    print(new_str)


if __name__ == '__main__':
    size = int(input())
    lista = []
    lista2 = []
    for i in range(0, size):
        vnes = input()
        for j in range(0, size):
            lista = vnes.split()
        lista2.append(lista)

    resenie(lista2)