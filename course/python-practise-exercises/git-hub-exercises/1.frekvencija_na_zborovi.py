def resenie(vlez):
    l = vlez.split()
    pominati=[]
    l.sort()
    flag=True

    for x in range(len(l)):
        num=0
        for j in range(len(pominati)):
            if pominati[j]==l[x]:
                flag=False
                continue
        if flag==True:
            for y in range(len(l)):
                if l[y]==l[x]:
                    num += 1
            print(l[x]+":"+str(num))
            pominati.append(l[x])
        flag=True

if __name__=="__main__":
    resenie("New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.")