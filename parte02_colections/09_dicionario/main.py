#NOTE - Diferente da lista, no dicionario voce aciona um texto a um significado
# A sintase certa é {'chave': "variavel", } ou {'chave': variavel_que_não_é_string, }

usuario = {
    'nome': "alex",
    'idade': 41,
    'altura': 1.72,
    'email': "alexgmail.com",
    'cpf': "123.456.789-12",
    'telefone': "(61) 9 9765-4321",
}
try:
    # Como exibir valor expecifico
    print(f"\nNome: {usuario['nome']}")
#NOTE - Sintaxe certa do print: print(f"texto {dicionario['chave']}") ou print(f"texto: {dicionario.get['chave]}")
    print(f"\nCPF? {usuario.get('cpf')}")   #NOTE - A sintaxe correta é .get()
                                            #NOTE - O .get[] ESTA ERRADO
#NOTE - O .get('var') serve exibir chaves que tem o risco de não existir sem crashar o programa
    for chave, valor in usuario.items():    #NOTE - O .items() enumera todas as chaves do dicionario
        print(f'{chave.capitalize()}: {valor}.') #NOTE -  .capitalize() Deixa apenas 1ª letra maiuscula da frase inteira

except Exception as e:
    print(f'error {e}')