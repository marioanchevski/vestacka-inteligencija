def briscola_score(round1,round2):
    points_round1=calculate(round1)
    points_round2=calculate(round2)
    print("Igrachot ima "+str(points_round1) +" poeni vo prvoto kolo.")
    print("Potrebno e da se osvojat najmalku "+str(121-points_round1)+" poeni vo vtoroto kolo.")
    print("Brojot na poeni na igrachot vo vtoroto kolo e "+ str(points_round2))


    if points_round1+points_round2==120:
        print("Vkupniot rezultate 120 poeni, sto e ist rezultat so protivnikot.")
        return "Draw!"
    elif points_round2>=121-points_round1:
        return "You Win!"
    elif points_round2<121-points_round1:
        return "You Lose!"

def calculate(list):
    points=0
    for x in list:
        pom = x[0]
        if pom=='A':
            points+=11
        elif pom=='3':
            points+=10
        elif pom=='K':
            points+=4
        elif pom=='Q':
            points+=3
        elif pom=='J':
            points+=2
        else:
            points+=0
    return points

if __name__=="__main__":
    print(briscola_score(
        ["Ac", "As", "3d", "3h", "3s", "Ah", "Kd"],
        ["3d", "Ad", "Ac", "As", "Ah"]
    ))
