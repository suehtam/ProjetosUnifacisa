opcao = 1

filmes = [ ]

while opcao != 6:
    print("\nLocadora de Goku")
    print("1) Listar \n2) Adicionar \n3) Pesquisar \n4) Remover \n5) Substituir \n6) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        if len(filmes) == 0:
            print("Não existem filmes a serem exibidos")
        else:
            print("Lista de Filmes")
            for item in filmes:
                print("-", item)

    elif opcao == 2:
        novoFilme = input("Digite o nome do novo filme: ")
        filmes.append(novoFilme)
        print("Filme adicionado com sucesso!")

    elif opcao == 3:
        codigo = int(input("Digite o código do filme a ser pesquisado: "))

        if codigo >= 1 and codigo <= len(filmes):
            filmePesquisado = filmes[codigo - 1]
            print("O filme pesquisado foi", filmePesquisado)
        else:
            print("O código informado é inválido.")

    elif opcao == 4:
        codigo = int(input("Digite o código do filme a ser removido: "))

        if codigo >= 1 and codigo <= len(filmes):
            filmes.pop(codigo - 1)
            print("O filme foi removido com sucesso!")

        else:
            print("O código informado é inválido.")

    elif opcao == 5:
        codigo = int(input("Digite o código do filme a ser substituído: "))

        if codigo >= 1 and codigo <= len(filmes):
            novoFilme = input("Digite o nome do novo filme: ")
            filmes[codigo - 1] = novoFilme
            print("Filme substituído com sucesso! ")

        else:
            print("O código informado é inválido.")

    elif opcao != 6:
        print("Opção Inválida")

print("Obrigado por usar a Locadora!")