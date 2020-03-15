def sovrshen_broj(broj):
    li = []
    zbir = 0
    for i in range(1,broj):
        if broj%i == 0:
            li.append(i)
            zbir = zbir+i

    if broj == zbir:
        return True
    else:
        return False

if __name__ == "__main__":
    broj = int(input())
    if sovrshen_broj(broj):
        print("Brojot",broj ,"e sovrshen")
    else:
        print("Brojot",broj ,"ne e sovrshen")