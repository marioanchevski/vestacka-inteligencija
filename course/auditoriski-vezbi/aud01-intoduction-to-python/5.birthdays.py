r = {
    "Borche":"27/01/1997",
     "Jovana":"14/09/1999"
    ,"Branko":"23/05/1996"
}
print("Dobredojdovte do rechnikot za rodendeni. Nie gi znaeme rodendenite na:")
for i in r.keys():
    print(i)
print("Koj rodenden e potrebno da se prebara?")
st = raw_input()
inf = r[st]
print(inf)
