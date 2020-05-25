def resenie1():
    n = int(input())
    m = int(input())
    matrix = []
    row = []
    for i in range(n):
        for j in range(m):
            row.append(int(input()))
        matrix.append(row)
        row = []
    print(matrix)
    matrix = [[elem * 2 for elem in nested] for nested in matrix]
    print(matrix)

def resenie2():
    n = int(input())
    m = int(input())

    elements_matrix = []
    for i in range(0, n):
        elements_row = [int(element) for element in input().split(" ")]
        # citame elementite kako string, go delime stringot po prazno mesto i sekoj element od listata go konvertirame vo int
        elements_matrix.append(elements_row)

    result_matrix = [elem * 2 for row in elements_matrix for elem in row]  # prv nacin - so ova se dobiva lista

    print(result_matrix)

    result_matrix_1 = [[elements_matrix[i][j] * 2 for j in range(0, m)] for i in range(0, n)]  # vtor nacin

    print(result_matrix_1)


if __name__=="__main__":
    resenie1()
