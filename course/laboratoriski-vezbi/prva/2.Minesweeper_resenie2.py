def predict_bomb(x, y, n, m):
    l = [[0] * m for i in range(n)]

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if is_predictable(i, j, n, m):
                l[i][j] += 1

    return l


def is_predictable(x, y, n, m):
    if x < 0 or x >= n:
        return False

    if y < 0 or y >= m:
        return False

    return True


def main():
    l = []
    size = int(input())
    for i in range(0, size):
        vnes = input()
        for j in range(0, size):
            lista = vnes.split()
        l.append(lista)

    predicted_separate = [predict_bomb(i, j, len(l), len(l[0])) for i in range(len(l)) for j in range(len(l[0])) if
                          l[i][j] == "#"]
    predicted_together = []

    for i in range(len(predicted_separate[0])):
        predicted_row = []

        for j in range(len(predicted_separate[0][0])):
            if l[i][j] == "#":
                predicted_row.append("#")
                continue

            counter = 0

            for k in range(len(predicted_separate)):
                counter += 1 if predicted_separate[k][i][j] else 0

            predicted_row.append(str(counter))

        predicted_together.append(predicted_row)

    new_str = ""
    for i in range(0, len(predicted_together)):
        new_str = new_str + "   ".join(predicted_together[i])
        new_str = new_str + "\n"

    print(new_str)


if __name__ == "__main__":
    main()
