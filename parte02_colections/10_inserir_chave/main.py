#dicionario
usuario = {
    'nome': "Fulano de Tal",
    'idade': 18,
    'email': "fulano@yahoo.com.br",
}

newky = input("\nInforme o nome da nova chave: ").strip().lower()

usuario[newky] = input("Insira o valor da nova chave: ").strip()

print("")
for chave, valor in usuario.items():
    print(f"{chave.capitalize()}: {valor}.")