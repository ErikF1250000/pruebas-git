#Lista uno
listaPersonas = ["Hana", "Sakura", "Yuri", "Yoh", "Hao", "Manta"]
i=0
for lista in listaPersonas:
    i += 1
    print(str(i)+ "- " + lista)

numPer = int(input("elige un numero de persona: "))

print(listaPersonas[(numPer - 1)])


