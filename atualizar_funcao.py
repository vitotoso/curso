produtos=[]
def cadastrar_produtos(produtos,nome,valor,quantidade,custo,imp1,imp2,taxa_lucro,frete,valor_final,imp3):
    
    produto={
        
        'Nome':nome,
        'Valor':valor,
        'Quantidade':quantidade,
        'Custo':custo,
        'Imp1':imp1,
        'Imp2':imp2,
        'Taxa_lucro':taxa_lucro,
        'Frete':frete,
        'Valor_final':valor_final,
        'Imp3':imp3
    }
    produtos.append(produto)

def imprimir_produtos(produto):
    for indice,produto in enumerate(produtos):
        print("==================================================")
        print(f"ID produto {indice}")
        print(f"Nome : {produto['Nome']}")
        print(f"valor : {produto['Valor']}")
        print(f"quantidade: {produto['Quantidade']}")
        print(f"imposto 1: {produto['Imp1']}")
        print(f"imposto 2: {produto['Imp2']}")
        print(f"imposto 3: {produto['Imp3']}")
        print(f"frete: {produto['Frete']}")
        print(f"Taxa de lucro: {produto['Taxa_lucro']}")
        print(f"custo: {produto['Custo']}")
        print(f"Valor final: {produto['Valor_final']}")
        print("==================================================")

def atualizar_produto(produtos,indice,nome,valor,quantidade,custo,imp1,imp2,taxa_lucro,frete,valor_final,imp3):
    if indice>=0 and indice<len(produtos):
        produtos[indice]['Nome']=nome
        produtos[indice]['Valor']=valor
        produtos[indice]['Quantidade']=quantidade
        produtos[indice]['Custo']=custo
        produtos[indice]['Imp1']=imp1
        produtos[indice]['Imp2']=imp2
        produtos[indice]['Taxa_lucro']=taxa_lucro
        produtos[indice]['Frete']=frete
        produtos[indice]['Valor_final']=valor_final
        produtos[indice]['Imp3']=imp3


while True:

    print("1  cadastrar produto")
    print("2  imprimir produto")
    print("3  atualizar produto")
    print("4  fechar programa")
    a = int(input("escolha sua ação: "))

    if a==1:

        nome = input("nome produto: ")
        quantidade=int(input("quantos produtos voce deseja vender?"))
        valor=float(input("qual o valor do seu produto: "))
        imp1=int(input("valor do primeiro imposto: "))
        imp2=int(input("valor do segundo imposto: "))
        imp3=int(input("valor do terceiro imposto "))
        taxa_lucro=int(input("taxa de lucro: "))
        frete=float(input("valor de frete: "))
        
        frete=frete/quantidade
       
        imp1=valor*(imp1/100)
        imp2=valor*(imp2/100)
        imp3=valor*(imp3/100)
        taxa_lucro=valor*(taxa_lucro/100)
        
        valor=valor+imp1+imp2+imp3+taxa_lucro
        valor=valor*quantidade
        valor_final=valor+frete
    
        custo=frete+imp1+imp2+imp3
        
        cadastrar_produtos(produtos,nome,valor,quantidade,custo,imp1,imp2,taxa_lucro,frete,valor_final,imp3)
    
    elif a==2:
        
        imprimir_produtos(produtos)
    
    elif a==3:
        
        indice=int(input("qual a posição do produto que vc deseja atualizar: "))
        nome = input("nome produto: ")
        quantidade=int(input("quantos produtos voce deseja vender?"))
        valor=float(input("qual o valor do seu produto: "))
        imp1=int(input("valor do primeiro imposto: "))
        imp2=int(input("valor do segundo imposto: "))
        imp3=int(input("valor do terceiro imposto "))
        taxa_lucro=int(input("taxa de lucro: "))
        frete=float(input("valor de frete: "))
        atualizar_produto(produtos,indice,nome,valor,quantidade,custo,imp1,imp2,taxa_lucro,frete,valor_final,imp3)
    else:
        break