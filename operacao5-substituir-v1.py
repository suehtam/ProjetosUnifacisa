filmes = [ "titanic", "lagoa azul", "trapalhões", "sonic" ]

codigo = int(input("Digite o código do filme a ser substituído: "))

if codigo >= 1 and codigo <= len(filmes):
    novoFilme = input("Digite o nome do novo filme: ")
    filmes[codigo-1] = novoFilme
    print("Filme substituído com sucesso! ")

else:
    print("O código informado é inválido.")