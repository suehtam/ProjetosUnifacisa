filmes = [ "titanic", "lagoa azul", "trapalhões", "sonic" ]

codigo = int(input("Digite o código do filme a ser removido: "))

if codigo >= 1 and codigo <= len(filmes):
    filmes.pop(codigo-1)
    print("O filme foi removido com sucesso!")

else:
    print("O código informado é inválido.")