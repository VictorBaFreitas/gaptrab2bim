produtos = []
vendas = []
venda_produtos = []
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

def inserir_venda():
    codigo_produto = input("Digite o código do produto: ")
    codigo_venda = input("Digite o código da venda: ")
    quantidade_prod = int(input("Insira a quantidade de produtos para a venda: "))
    
    if verifica_codigo_venda(codigo_venda):
        print("Código venda já existente. Não é possível cadastrar á venda.")
    else:
        if quantidade_prod <= 0:
            print("A quantidade vendida deve ser maior que zero.")
            return
        else:
            if verificar_codigo_produto(codigo_produto):
                for produto in produtos:
                    if produto['codigo_prod'] == codigo_produto:
                        valor = produto['preco_prod']                        
                venda = {'codigo_venda': codigo_venda, 'quantidade_prod': quantidade_prod}
                vendas.append(venda)
                venda_produto = {'codigo_venda': codigo_venda, 'codigo_prod': codigo_produto, 'valor_total': quantidade_prod*valor}
                venda_produtos.append(venda_produto)
                print("Venda Cadastrada com Sucesso!")
            else:
                print("Produto não Encontrado!")   


#-------------------------------verifica------------------------------------------//

def verificar_codigo_produto(codigo_prod):
    for produto in produtos:
        if produto['codigo_prod'] == codigo_prod:
            return True
    return False

def verifica_codigo_venda(codigo_venda):
    for venda in vendas:
        if venda['codigo_venda'] == codigo_venda:
            return True
    return False

#-------------------------------listar por código------------------------------------------//

def listar_produto_por_codigo(codigo_prod):
    for produto in produtos:
        if produto['codigo_prod'] == codigo_prod:
            print("Código: {}, Nome: {}, Preço: R${}".format(produto['codigo_prod'], produto['nome_prod'], produto['preco_prod']))
            return
    print("Produto não encontrado!")

def listar_venda_por_codigo(codigo_venda):
    for venda in vendas:
        if venda['codigo_venda'] == codigo_venda:
            print("Código: {}, Quantidade: {}".format(venda['codigo_venda'], venda['quantidade_prod']))
    for venda_produto in venda_produtos:
        if venda_produto['codigo_venda'] == codigo_venda:
            print("Valor Total R$: {}".format(venda_produto['valor_total']))
            return
    print("Venda não encontrada!")

#----------------------------------excluir---------------------------------------//

def excluir_produto_por_codigo(codigo_prod):
    for venda_produto in venda_produtos:
        if venda_produto['codigo_prod'] == codigo_prod:
            print('Venda existente neste código!')
            return
    for produto in produtos:
        if produto['codigo_prod'] == codigo_prod:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado!")

def excluir_venda_por_codigo(codigo_venda):
    for venda in vendas:
        if venda['codigo_venda'] == codigo_venda:
            vendas.remove(venda)
    for venda_produto in venda_produtos:
        if venda_produto['codigo_venda'] == codigo_venda:
            venda_produtos.remove(venda_produto)
            print("Venda Excluída com Sucesso!")
            return
    print("Venda não encontrada!")

#-----------------------------------alterar--------------------------------------//

def alterar_produto_por_codigo(codigo_prod):
    for venda_produto in venda_produtos:
        if venda_produto['codigo_prod'] == codigo_prod:
            print('Venda existente neste código!')
            return
    for produto in produtos:
        if produto['codigo_prod'] == codigo_prod:
            print("Produto encontrado. Insira as novas informações:")
            nome_prod = input("Digite o novo nome do produto: ")
            preco_prod = float(input("Digite o novo preço do produto: "))
            produto['nome_prod'] = nome_prod
            produto['preco_prod'] = preco_prod
            print("Produto alterado com sucesso!")
            return
    print("Produto não encontrado!")

def alterar_venda_por_codigo(codigo_venda):
    if verifica_codigo_venda(codigo_venda):
        for venda in vendas:
            if venda['codigo_venda'] == codigo_venda:
                print("Venda encontrada! Insira as novas informações: ")
                quantidade_prod = int(input("Digite a nova quantidades de produtos: "))
                venda['quantidade_prod'] = quantidade_prod

        for venda_produto in venda_produtos:
            if venda_produto['codigo_venda'] == codigo_venda:
                codigo_produto = venda_produto['codigo_prod']

        for produto in produtos:
            if produto['codigo_prod'] == codigo_produto:
                preco = produto['preco_prod']

        for venda_produto in venda_produtos:
            if venda_produto['codigo_venda'] == codigo_venda:
                venda_produto['valor_total'] = quantidade_prod*preco
                print("Venda alterado com sucesso!")
    else:
        print("Venda não encontrada!")

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

def cadastro_venda():
    while True:
        print("\n----- MENU VENDA ------")
        print("1 - Inserir venda")
        print("2 - Listar todas vendas")
        print("3 - Listar venda por código")
        print("4 - Excluir Venda")
        print("5 - Alterar Venda")
        print("0 - Sair")

        opcao = input("Escolhe uma opção: ")

        if opcao == "1":
            inserir_venda()
        elif opcao == "2":
            print("Vendas cadastradas: ")
            for venda in vendas:
                print("Código Venda: {}, Quantidade: {}".format(venda['codigo_venda'], venda['quantidade_prod']))
            for venda_produto in venda_produtos:
                print("Valor Total R$: {}".format(venda_produto['valor_total']))
        elif opcao == "3":
            codigo_venda = input("Digite o código da venda que deseja listar: ")
            listar_venda_por_codigo(codigo_venda)
        elif opcao == "4":
            codigo_venda = input("Digite o código da venda que deseja excluir: ")
            excluir_venda_por_codigo(codigo_venda)
        elif opcao == "5":
            codigo_venda = input("Digite o código da venda que deseja alterar: ")
            alterar_venda_por_codigo(codigo_venda)
        elif opcao == "0":
            return False
        else:
            print("Opção inválida!")


while True:
    print ("\n----- MENU PRINCIPAL -----")
    print ("1 - Inserir um novo Produto")
    print ("2 - Inserir uma nova Venda")
    print ("0 - Sair")

    opcao = input("Escolha uma Opção: ")

    if opcao == "1":
        cadastro_produto()
    elif opcao == "2":
        cadastro_venda()
    elif opcao == "0":
        break
    else:
        print("Opção inválida!")