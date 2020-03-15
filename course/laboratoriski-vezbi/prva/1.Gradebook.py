def pecati():
    cur_index = ""
    flag = False
    pominati_indeksi = []

    for j in range(len(list_students)):
        cur_index = str(list_students[j]['indeks'])
        for l in range(len(pominati_indeksi)):
            if pominati_indeksi[l] == cur_index:
                flag = True
                break
        if flag == False:
            print("Student: " + list_students[j]['ime'])
            for x in range(len(list_students)):
                if cur_index == list_students[x]['indeks']:
                    print("\t" + list_students[x]['predmet'] + ": " + str(list_students[x]['ocenka']))
            pominati_indeksi.append(cur_index)
            print()
        flag = False


if __name__ == '__main__':
    studenti = {}
    list_students = []
    vnesi = input()
    index = 0
    while vnesi != 'end':
        inf = vnesi.split(",")
        studenti['ime'] = inf[0] + " " + inf[1]
        studenti['indeks'] = inf[2]
        index = str(inf[2])
        studenti['predmet'] = inf[3]

        bodovi = int(int(inf[4]) + int(inf[5]) + int(inf[6]))
        if bodovi >= 0 and bodovi <= 50:
            studenti['ocenka'] = 5
        elif bodovi >= 50 and bodovi <= 60:
            studenti['ocenka'] = 6
        elif bodovi > 60 and bodovi <= 70:
            studenti['ocenka'] = 7
        elif bodovi > 70 and bodovi <= 80:
            studenti['ocenka'] = 8
        elif bodovi > 80 and bodovi <= 90:
            studenti['ocenka'] = 9
        elif bodovi > 90 and bodovi <= 100:
            studenti['ocenka'] = 10
        vnesi = input()
        list_students.append(dict(studenti))

    pecati()

