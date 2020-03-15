import math
def  resenie(tablica,m,n):

    for i in range(m,n+1):
        torka=(i*i,i*i*i,round(math.sqrt(i),5))
        tablica[i]=torka
    return tablica


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    x = int(input())
    # vasiot kod pisuvajte go tuka
    tablica = {}
    resenie(tablica,m,n)
    if x<m or x>n:
        print("nema podatoci")
    else:
    	print(tablica[x])
    print(sorted(tablica.items()))