while True:
    nota = float(input("digite uma nota de 0 a 10:"))

    if nota>=0 and nota<=10:
        print ("nota valida")
        break

    else:
        print("nota invalida")