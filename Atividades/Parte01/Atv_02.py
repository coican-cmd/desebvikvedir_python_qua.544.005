# atividade 02 - Cinema com classificação indicativa

# Cada filme: (nome, sala, idade mínima, texto da classificação)
filmes = [
    ("Divertida Mente 2", 1, 0, "Livre"),
    ("Moana 2", 2, 10, "10 anos"),
    ("Homem-Aranha: Sem Volta Para Casa", 3, 12, "12 anos"),
    ("Jogos Vorazes", 4, 14, "14 anos"),
    ("Coringa", 5, 18, "18 anos"),
]

# Nome e idade são informados uma única vez
nome = input("Digite seu nome: ").strip()

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if idade >= 0:
            break
        print("A idade não pode ser negativa.")
    except ValueError:
        print("Digite apenas números inteiros.")

ingresso_emitido = False

while not ingresso_emitido:
    print("\n=== FILMES EM CARTAZ ===")
    for titulo, sala, idade_min, classificacao in filmes:
        print(f"Sala {sala} | {titulo} | Classificação: {classificacao}")

    try:
        escolha = int(input("\nEscolha o número da sala do filme desejado: "))
    except ValueError:
        print("Opção inválida! Digite o número da sala.")
        continue

    # Procura o filme da sala escolhida
    filme_escolhido = None
    for filme in filmes:
        if filme[1] == escolha:
            filme_escolhido = filme
            break

    if filme_escolhido is None:
        print("Sala inexistente! Tente novamente.")
        continue

    titulo, sala, idade_min, classificacao = filme_escolhido

    if idade >= idade_min:
        print("\n" + "=" * 32)
        print("          INGRESSO")
        print("=" * 32)
        print(f"Nome:          {nome}")
        print(f"Idade:         {idade} anos")
        print(f"Filme:         {titulo}")
        print(f"Sala:          {sala}")
        print(f"Classificação: {classificacao}")
        print("=" * 32)
        print("Bom filme!")
        ingresso_emitido = True
    else:
        print(f"\nEntrada negada, {nome}! '{titulo}' é para maiores de {idade_min} anos.")
        print("Escolha outro filme.")
        

# TODO: atividade 02
'''
Crie um programa em que o usuario informe uma unica vez o nome e a idade , e em seguida, o programa exibe uma lista de 5 filmes do cinema e suas em seguida, o programa exibe uma lista de 5 filmes do cinema e suas respectivas salas e classificações indicativas.
O usuario devera escolher a sala do filme desejado. Se tiver a idade minima, o programa imprime o ingresso e encerra. Senão, o programa impede a entrada do usuario e retorna a lista para que o mesmo possa escolher ouro filme'''