valor_final[]
produto=[]
imposto1=[]
imposto2=[]
imposto3=[]
frete=[]
valor=[]
lucro=[]
quantidade[]

while True:

    print("cadastrar produto(s)   1")
    print("imprimir   2")
    print("fechar programa   3")
    a=int(input("digite o sua ação: "))

    if a == 1:
       
       
        produto=str(input("qual produto voce deseja cadastrar?: "))
        produto.append(produto)
        valor=float(input("quanto ira custar o seu produto?: "))
        valor.append(valor)
        quantidade=int(input("quantas unidades do produto voce deseja vender?:"))
        quantidade.append(quantas)
        imposto1=int(input("qual o valor do primeiro imposto?: "))
        imposto1.append(imposto1)
        imposto2=int(input("qual o valor do segundo imposto?: "))
        imposto2.append(imposto2)
        imposto3=int(input("qual o valor do terceiro produto?: "))
        imposto3.append(imposto3)
        frete=float(input("qual o valor do frete do seu prduto?: "))
        frete.append(frete)
        lucro=int(input("qual a taxa de lucro voce deseja inserir?: "))
        lucro.append(lucro)
        
        'frete=frete/quantidade
       
        imposto1=valor*(imposto1/100)
        imposto2=valor*(imposto2/100)
        imposto3=valor*(imposto3/100)
        lucro=valor*(lucro/100)
        
        valor=valor+imposto1+imposto2+imposto3+lucro
        calculo_valor=valor*quantidade
        valor_final=calculo_valor+frete
        
        valor_final.append(valor_final)
    
    elif a == 2:

        for i in range (len(produto))

            print(f"{prduto[i]}    R$ {valor_final[i]}")

            print("--------------------------------------------")
        

