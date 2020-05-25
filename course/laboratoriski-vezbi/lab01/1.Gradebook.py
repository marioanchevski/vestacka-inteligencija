def pecati(students):

    flag = False
    pominati_indeksi = []

    for i in range(len(students)):
        cur_index = str(students[i]['indeks'])
        for j in range(len(pominati_indeksi)):
            if pominati_indeksi[j] == cur_index:
                flag = True
                break
        if flag == False:
            print("Student: " + students[i]['ime'])
            for x in range(len(students)):
                if cur_index == students[x]['indeks']:
                    print("\t" + students[x]['predmet'] + ": " + str(students[x]['ocenka']))
            pominati_indeksi.append(cur_index)
            print()
        flag = False

def vnesi():
    studenti = {}
    list_students = []
    vnesi = input()
    while vnesi != 'end':
        inf = vnesi.split(",")
        studenti['ime'] = inf[0] + " " + inf[1]
        studenti['indeks'] = inf[2]
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
    return list_students

if __name__ == '__main__':
    students=vnesi()
    pecati(students)

