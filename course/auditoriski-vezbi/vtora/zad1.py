if __name__=="__main__":
    t=[('a',1),('b',2),('c',3)]
    print(t)
    t=[(x,y) for y,x in t]
    print(t)
