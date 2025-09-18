from operacoesbd import *

opcao = 1
conn = criarConexao('localhost','root','admin','gestao_ouvidoria')

while opcao != 6:
    print("\n 1) Listar, 2) Pesquisar pelo Codigo, 3) Inserir, 4) Remover 5) Quantidade 6) Sair")
    opcao = int(input("Digite a opcao: "))

    if opcao == 1:
        consulta = "select * from ouvidoriaBD"
        filmes = listarBancoDados(conn, consulta)

        if len(filmes) == 0:
            print("Não existem filmes cadastrados")
        else:
            for item in filmes:
                print('Nome do filme', item[1], 'lancado no ano', item[3])

    elif opcao == 2:
        codigoFilme = int(input("Digite o codigo do filme: "))
        consulta = "select * from Filmes where codigo = %s "
        valores = [codigoFilme]
        filmes = listarBancoDados(conn, consulta, valores)

        if len(filmes) == 0:
            print("Nao existe filme para o codigo informado")
        else:
            for item in filmes:
                print('Nome do filme', item[1], 'lancado no ano', item[3])

    elif opcao == 3:
        nomeFilme = input("Digite o nome do filme: ")
        sinopseFilme = input("Digite a sinopse do filme: ")
        anoFilme = int(input("Digite o ano do filme: "))

        consulta = 'insert into Filmes (titulo,sinopse,ano) values (%s,%s,%s)'
        valores = [nomeFilme, sinopseFilme, anoFilme]

        codigoFilme = insertNoBancoDados(conn, consulta, valores)
        print("Filme adicionado com sucesso! O código é", codigoFilme)

    elif opcao == 4:
        codigoFilme = int(input("Digite o codigo do filme a ser removido: "))

        consulta = 'delete from Filmes where codigo  = %s'
        valores = [codigoFilme]

        filmesRemovidos = excluirBancoDados(conn, consulta, valores)

        if filmesRemovidos == 1:
            print("Filme removido com sucesso!")
        else:
            print("Filme nao existe.")

    elif opcao == 5:
        consulta = "select count(*) from Filmes"
        quantidadeFilmes = listarBancoDados(conn, consulta)

        print("Atualmente, temos", quantidadeFilmes[0][0], "filme(s)")

    elif opcao != 6:
        print("Opção Inválida")

encerrarConexao(conn)
print("Obrigado por usar a Locadora de José do Egito")