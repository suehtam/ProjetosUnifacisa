# ouvidoria.py
from operacoesbd import listarBancoDados, insertNoBancoDados, excluirBancoDados, atualizarBancoDados

def listarManifestacoes(conn):
    linhas = listarBancoDados(conn, "SELECT * FROM ouvidoriaBD;")
    if not linhas:
        print("Não existem manifestações cadastradas.")
    else:
        for codigo, nome, assunto, texto, respondente, tipo in linhas:
            print(f"\nCódigo: {codigo}\nNome: {nome}\nAssunto: {assunto}\nManifestação: {texto}\nRespondente: {respondente}\nTipo: {tipo}")

def adicionarManifestacao(conn):
    nome        = input("Seu nome: ").strip().capitalize()
    assunto     = input("Assunto: ").strip().capitalize()
    texto       = input("Manifestação: ").strip().capitalize()

    # valida respondente
    op = None
    while op not in ('1','2','3'):
        op = input("\nQuem te atendeu? 1-Evandro  2-Matheus  3-Rafael: ").strip()
    respondente = {'1':'Evandro','2':'Matheus','3':'Rafael'}[op]

    # valida tipo
    op = None
    while op not in ('1','2','3'):
        op = input("Tipo de manifestação? 1-Reclamação  2-Elogio  3-Sugestão: ").strip()
    tipo = {'1':'Reclamação','2':'Elogio','3':'Sugestão'}[op]

    sql     = "INSERT INTO ouvidoriaBD(nome,assunto,manifestacao,respondente,tipo) VALUES (%s,%s,%s,%s,%s)"
    valores = (nome, assunto, texto, respondente, tipo)
    novo_id = insertNoBancoDados(conn, sql, valores)
    print(f"Manifestação cadastrada com código {novo_id} com sucesso.")

def pesquisarManifestacoes(conn):
    codigo = int(input("Digite o código: "))
    sql    = "SELECT * FROM ouvidoriaBD WHERE codigo = %s"
    linhas = listarBancoDados(conn, sql, (codigo,))
    if linhas:
        item = linhas[0]
        print(f"\nEncontrado: Código {item[0]}, Assunto {item[2]}, Texto {item[3]}")
    else:
        print("Manifestação não encontrada.")

def removerManifestacoes(conn):
    codigo = int(input("Código a remover: "))
    confirm = input("Confirmar exclusão? (s/n): ").strip().lower()
    if confirm == 's':
        sql  = "DELETE FROM ouvidoriaBD WHERE codigo = %s"
        cont = excluirBancoDados(conn, sql, (codigo,))
        if cont:
            print("Excluído com sucesso.")
        else:
            print("Nada foi excluído.")
    else:
        print("Operação cancelada.")

def substituirManifestacoes(conn):
    codigo = int(input("Código a atualizar: "))
    novo_texto = input("Novo texto da manifestação: ").strip().capitalize()
    sql   = "UPDATE ouvidoriaBD SET manifestacao = %s WHERE codigo = %s"
    cont  = atualizarBancoDados(conn, sql, (novo_texto, codigo))
    if cont:
        print("Manifestação atualizada.")
    else:
        print("Nada foi alterado ou código não existe.")
