def cadastrar_cliente(cliente,nome,email,telefone):
    cliente ={
        'Nome':nome,
        'Email':email,
        'Telefone':telefone

    }
    clientes.append(cliente)
    print("Cliente cadastrado com sucesso")  
def imprimir_cliente(clientes):
    for indice,cliente in enumerate(clientes):
        print("====================================")
        print(f"ID cliente {indice+1}")
        print(f"Nome: {cliente['Nome']}")
        print(f"Email: {cliente['Email']}")
        print(f"Telefone: {cliente['Telefone']}")
        print("====================================")

clientes=[]
nome = input("digite o nome: ")
email = input("digite o email: ")
telefone = input("digite o numero: ")
cadastrar_cliente(clientes,nome,email,telefone)
imprimir_cliente(clientes)
