Numero_inicio=int(input("numero de inicio:"))
Numero_parada=int(input("numero de parada:"))

soma=0

if Numero_inicio % 2 == 0:

    for i in range (Numero_inicio,Numero_parada,2):

        soma=soma+i

        print(soma)

else:

    for i in range (Numero_inicio,Numero_parada,2):

        soma=soma+i

        print(soma)    