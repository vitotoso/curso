pais1=float(input("quantidade de habitantes do país:"))
crescimento1=float(input("tamanho em porcentagem de crescimento por ano:"))
pais2=float(input("quantidade de habitantes do país:"))
crescimento2=float(input("tamanho em porcentagem de crescimento por ano:"))
ano=0


if pais1>pais2:

    while pais1>=pais2:

        pais1+=pais1*(crescimento1/100)
        pais2+=pais2*(crescimento2/100)
        ano=ano+1
    print(ano)

else:

    while pais2>=pais1:
        
        pais1+=pais1*(crescimento1/100)
        pais2+=pais2*(crescimento2/100)     
        ano=ano+1
    print(ano)