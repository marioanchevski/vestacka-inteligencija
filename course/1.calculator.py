operations = ['+', '-', '*', '/', '%', '//', '**']


def solution(x, y, oper):
    if oper not in operations:
        print("INVALID ARGUMENTS")
        return 0

    result = 0
    if oper == '+':
        return x + y
    elif oper == '-':
        return x - y
    elif oper == '/':
        return x / y
    elif oper == '*':
        return x * y
    elif oper == '%':
        return x % y
    elif oper == '**':
        return x ** y
    elif oper == '//':
        return x // y


if __name__ == "__main__":
    x = float(input())
    oper = input()
    y = float(input())
    rez = solution(x, y, oper)
    if rez != 0:
        print("Resultat:", rez)
