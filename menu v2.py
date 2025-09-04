# 1) Listar

manifestacoes =[]
print("Lista de manifestações")
while True:
    print(f'\n1) Listar \n2) Adicionar \n3) Pesquisar manifestações \n4) Remover manifestações \n5) Substituir manifestações \n6) Sair')

    opcao = int(input("Digite a opção: "))
    listar = 0

    if opcao == 1:
        if len(manifestacoes) > 0:
            print(f'\nLista de manifestações')
            for item in manifestacoes:
                listar = listar + 1
                print(f'{listar} - {item}')
        else:
            print(f'Não há manifestações a serem listadas!')

    elif opcao == 2:
        novaManifestacao = input(f'Digite a sua manisfetação: ').capitalize()
        manifestacoes.append(novaManifestacao)
        print(f'Nova manifestação adicionada com sucesso.')

    elif opcao == 3:
        codigo = int(input(f'Digite o código da manifestação: '))
        if codigo > 0 and codigo <= len(manifestacoes):
            print(f'A manifestação pesquisada é: {manifestacoes[codigo - 1]}.')
        else:
            print(f'A manifestação não existe!')

    elif opcao == 4:
        codigo = int(input(f'Digite o código da manifestação que deseja remover: '))
        if codigo > 0 and codigo <= len(manifestacoes) :
            confirmar = int(input(f'Deseja remover "{manifestacoes[codigo - 1]}"? 1- Sim 2- Não: '))
            if confirmar == 1:
                manifestacoes.pop(codigo-1)
                print(f'Manifestação removida com sucesso.')
            elif confirmar == 2:
                print(f'Manifestação não foi removida!')
            else:
                print(f'Opção inválida!')
        else:
            print(f'Não existe manifestação com esse código!')

    elif opcao == 5:
        codigo = int(input(f'Digite o código da manifestação que deseja substituir: '))
        if codigo > 0 and codigo <= len(manifestacoes):
            confirmar = int(input(f'Deseja substituir "{manifestacoes[codigo - 1]}"? 1- Sim 2- Não: '))
            if confirmar == 1:
                manifestacoes[codigo - 1] = input(f'Digite a manifestação que irá substituir: ').capitalize()
                print(f'Manifestação substituído com sucesso.')
            elif confirmar == 2:
                print(f'Manifestação não foi removida!')
            else:
                print(f'Opção inválida!')
        else:
            print(f'Não existe manifestação com esse código!')

    elif opcao == 6:
        break

    else:
        print(f'\nOpção inválida!')


print(f'Obrigado por utilizar!')
