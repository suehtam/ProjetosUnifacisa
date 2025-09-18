# 1) listagem
from turtledemo.rosette import mn_eck

from operacoesbd import *
from ouvidoria import *

conn = criarConexao('127.0.0.1', 'root', 'admin', 'gestao_ouvidoria')
manifestacoes =[]
print("Bem Vindo ao Menu de Manifestações")
while True:
    print(f'\n1) Listar \n2) Adicionar \n3) Pesquisar manifestações \n4) Remover manifestações \n5) Substituir manifestações \n6) Sair')

    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        listaDeManifestacoes(manifestacoes)

    elif opcao == 2:
        adicionarManifestacao(manifestacoes)

    elif opcao == 3:
        pesquisarManifestacoes(manifestacoes)

    elif opcao == 4:
        removerManifestacoes(manifestacoes)

    elif opcao == 5:
        substituirManifestacoes(manifestacoes)

    elif opcao == 6:
        break

    else:
        print(f'\nOpção inválida!')

print(f'Obrigado por utilizar!')
encerrarConexao(conn)