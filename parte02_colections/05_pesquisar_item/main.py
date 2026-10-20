# lista
cidades = [
    'Taguatinga',
    'Plano Piloto',
    'Santa maria',
    'Gama',
    'Samambaia',
    'Santa maria',
    'Taguatinga',
    'Planaltina',
    'Plano Piloto',
    'Brazlãndia',
    'Plano Piloto'
]


# usuario informa o item  a ser pesquisado
item = input("Informe a cidade a ser pesquisada: ").strip().title()

# verifica quantas vezes o termo foi encontrado e informa na tela
print(f"{item} foi encontrado {cidades.count(item)} vezes na lista.")
