# Lista de dicionários
usuarios = [
    {
        'nome': "Alex Machado",
        'idade': 41,
        'email': "alex@gmail.com",
    },
    {
        'nome': "Joana da Silva",
        'idade': 18,
        'email': "joana@gmail.com",
    },
    {   'nome': "Karolyne de Souza",
        'idade': 21,
        'email': "karol@gmail.com",

    },
]

for usuario in usuarios:
    for chave, valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")