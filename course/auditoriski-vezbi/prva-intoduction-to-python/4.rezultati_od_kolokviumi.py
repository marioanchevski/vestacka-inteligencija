def suma_kolokviumi(rezultati):
    for i in rezultati:
        i["Vkupno od kolokviumi"] = i["Kolokvium 1"] + i["Kolokvium 2"]
        del i["Kolokvium 1"]
        del i["Kolokvium 2"]
    return rezultati

# your code here


if __name__ == "__main__":
    n = int(input())
    rezultati = []  # ova e listata od rechnici
    for i in range(0, n):
        r = {}  # rechnik koj kje chuva podatoci za eden student
        brojIndeks = input()
        brojPoeni1 = float(input())
        brojPoeni2 = float(input())
        # ovde dodadete gi podatocite vo rechnikot. Potoa dodadete go rechnikot vo listata rezultati!!
        r["indeks"]=brojIndeks
        r["Predmet"]="Veshtachka inteligencija"
        r["Kolokvium 1"]=brojPoeni1
        r["Kolokvium 2"]=brojPoeni2
        rezultati.append(r)

    print(suma_kolokviumi(rezultati))