from operacoesbd import *

def listarManifestacoes(conn):
    print(f'\nLista de manifestações')
    consulta = "select * from ouvidoriaBD;"
    manifestacoes = listarBancoDados(conn, consulta)

    if len(manifestacoes) == 0:
        print(f"\nNão existem manifestações cadastradas")
    else:
        for item in manifestacoes:
            print(f'\nAssunto da Manifestação: \n{item[1]} \nManifestação: \n{item[2]}')

def adicionarManifestacao(conn):
    nome = input("Digite o seu nome: ").capitalize()

    assunto = input("Digite o assunto: ").capitalize()
    manifestacao = input("Digite a manifestação: ").capitalize()

    respondente = int(input(f'\nQual respondente te atendeu? \n1) Evandro \n2) Matheus \n3) Rafael\n: '))
    confirmacao = [1,2,3]
    while respondente in confirmacao:
        if respondente == 1:
            respondente = str('Evandro')
            break
        elif respondente == 2:
            respondente = str('Matheus')
            break
        elif respondente == 3:
            respondente = str('Rafael')
            break
        else:
            print(f'Número inválido, digite novamente!')
        respondente = int(input(f'\nQual respondente te atendeu? \n1) Evandro \n2) Matheus \n3) Rafael\n: '))
    tipo = int(input(f'Selecione o tipo da sua manifestção \n1) Reclamação \n2) Elogio \n3) Sugestão\n: '))
    while tipo in confirmacao:
        if tipo == 1:
            tipo = str('Elogio')
            break
        elif tipo == 2:
            tipo = str('Reclamação')
            break
        elif tipo == 3:
            tipo = str('Sugestão')
            break
        else:
            print(f'Número inválido, digite novamente!')
        tipo = int(input(f'Selecione o tipo da sua manifestção \n1) Reclamação \n2) Elogio \n3) Sugestão\n: '))
    insere = 'insert into ouvidoriaBD(nome,assunto,manifestacao,respondente,tipo) values(%s,%s,%s,%s,%s)'
    valores = [nome, assunto, manifestacao, respondente, tipo]
    novaManifestacao = insertNoBancoDados(conn, insere, valores)
    print(f'Nova manifestação adicionada com sucesso.')

def pesquisarManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação: '))
    comando = "select * from ouvidoriaBD where codigo = %s"
    lista = [codigo]
    manifestacoes = listarBancoDados(conn, comando, lista)

    if len(manifestacoes) != 0:
        print(f'\nA manifestação pesquisada é: {manifestacoes[codigo - 1]}.')
    else:
        print(f'A manifestação não existe!')

def removerManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação que deseja remover: '))
    comando = "select * from ouvidoriaBD where codigo = %s"
    lista = [codigo]
    manifestacoes = listarBancoDados(conn, comando, lista)

    if codigo > 0 and codigo <= len(manifestacoes):
        confirmacao = int(input(f'Deseja remover "{manifestacoes[codigo - 1]}"? 1- Sim 2- Não: '))
        if confirmacao == 1:
            comando = "delete from ouvidoriaBD where codigo = %s"
            lista = [codigo]
            manifestacoes = listarBancoDados(conn, comando, lista)
        elif confirmacao == 2:
            print(f'Manifestação não foi removida!')
        else:
            print(f'Opção inválida!')
    else:
        print(f'Opção inválida!')

    if codigo > 0 and codigo <= len(manifestacoes):
        confirmacao = int(input(f'Deseja remover "{manifestacoes[codigo - 1]}"? 1- Sim 2- Não: '))
        if confirmacao == 1:
            manifestacoes.pop(codigo - 1)
            print(f'Manifestação removida com sucesso.')
        elif confirmacao == 2:
            print(f'Manifestação não foi removida!')
        else:
            print(f'Opção inválida!')
    else:
        print(f'Não existe manifestação com esse código!')

def substituirManifestacoes(conn):
    codigo = int(input(f'Digite o código da manifestação que deseja substituir: '))
    if codigo > 0 and codigo <= len(manifestacoes):
        confirmacao = int(input(f'Deseja substituir "{manifestacoes[codigo - 1]}"? 1- Sim 2- Não: '))
        if confirmacao == 1:
            manifestacoes[codigo - 1] = input(f'Digite a manifestação que irá substituir: ').capitalize()
            print(f'Manifestação substituído com sucesso.')
        elif confirmacao == 2:
            print(f'Manifestação não foi removida!')
        else:
            print(f'Opção inválida!')
    else:
        print(f'Não existe manifestação com esse código!')


