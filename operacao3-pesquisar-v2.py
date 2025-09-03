filmes = [ "titanic", "lagoa azul", "trapalhões", "sonic" ]

codigo = int(input("Digite o código do filme a ser pesquisado: "))

if codigo >= 1 and codigo <= len(filmes):
    filmePesquisado = filmes[codigo-1]
    print("O filme pesquisado foi", filmePesquisado)
else:
    print("O código informado é inválido.")