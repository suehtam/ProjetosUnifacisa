opcao = 1

while opcao != 6:
    print("\nLocadora de Goku")
    print("1) Listar \n2) Adicionar \n3) Pesquisar \n4) Remover \n5) Substituir \n6) Sair")
    opcao = int(input("Digite a sua opção: "))

    if opcao == 1:
        print("Listar")

    elif opcao == 2:
        print("Adicionar")

    elif opcao == 3:
        print("Pesquisar")

    elif opcao == 4:
        print("Remover")

    elif opcao == 5:
        print("Substituir")

    elif opcao != 6:
        print("Opção Inválida")

print("Obrigado por usar a Locadora!")