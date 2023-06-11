produtos = []

#-------------------------------inserir------------------------------------------//

def inserir_produto():
    codigo_prod = input("Digite o código do produto: ")
    nome_prod = input("Digite o nome do produto: ")
    preco_prod = float(input("Digite o preço do produto: "))

    if verificar_codigo_produto(codigo_prod):
        print("Código já existente. Não é possível cadastrar o produto.")
    else:
        produto = {'codigo_prod': codigo_prod, 'nome_prod': nome_prod, 'preco_prod': preco_prod}
        produtos.append(produto)
        print("Produto cadastrado com sucesso!")

#-------------------------------verifica------------------------------------------//

def verificar_codigo_produto(codigo_prod):
    for produto in produtos:
        if produto['codigo_prod'] == codigo_prod:
            return True
    return False

#-------------------------------listar por código------------------------------------------//

def listar_produto_por_codigo(codigo_prod):
    for produto in produtos:
        if produto['codigo_prod'] == codigo_prod:
            print("Código: {}, Nome: {}, Preço: R${}".format(produto['codigo_prod'], produto['nome_prod'], produto['preco_prod']))
            return
    print("Produto não encontrado!")

#----------------------------------excluir---------------------------------------//

def excluir_produto_por_codigo(codigo_prod):
    for produto in produtos:
        if produto['codigo_prod'] == codigo_prod:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado!")

#-----------------------------------alterar--------------------------------------//

def alterar_produto_por_codigo(codigo):
    for produto in produtos:
        if produto['codigo_prod'] == codigo:
            print("Produto encontrado. Insira as novas informações:")
            nome_prod = input("Digite o novo nome do produto: ")
            preco_prod = float(input("Digite o novo preço do produto: "))
            produto['nome_prod'] = nome_prod
            produto['preco_prod'] = preco_prod
            print("Produto alterado com sucesso!")
            return
    print("Produto não encontrado!")

#------------------------------------menus-------------------------------------//

def cadastro_produto():
    while True:
        print("\n----- MENU PRODUTO -----")
        print("1 - Inserir produto")
        print("2 - Listar todos Produtos")
        print("3 - Listar produto por código")
        print("4 - Excluir Produto")
        print("5 - Alterar Produto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            inserir_produto()
        elif opcao == "2":
            print("Produtos cadastrados:")
            for produto in produtos:
                print("Código: {}, Nome: {}, Preço: R${}".format(produto['codigo_prod'], produto['nome_prod'], produto['preco_prod']))
        elif opcao == "3":
            codigo_produto = input("Digite o código do produto que deseja listar: ")
            listar_produto_por_codigo(codigo_produto)
        elif opcao == "4":
            codigo_produto = input("Digite o código do produto que deseja excluir: ")
            excluir_produto_por_codigo(codigo_produto)
        elif opcao == "5":
            codigo_produto = input("Digite o código do produto que deseja alterar: ")
            alterar_produto_por_codigo(codigo_produto)
        elif opcao == "0":
            return False
        else:
            print("Opção inválida!")

while True:
    print ("\n----- MENU PRINCIPAL -----")
    print ("1 - Inserir um novo Produto")
    print ("0 - Sair")

    opcao = input("Escolha uma Opção: ")

    if opcao == "1":
        cadastro_produto()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")