import os

usuario = {
    'nome': "Thomas Anderson",
    'idade': 40,
    'email': "mranderson@gmail.com",
    'telefone': "(61) 96666-6666",
}

# loop
while True:

    os.system("cls" if os.name == "nt" else "clear")
    for chave, valor in usuario.items()
        print(f"{chave}: {valor};")
    #for n, chave in usuario.items(): #NOTE - Serve para exibir o menu
    #verifica se a chave é valida
    #Informar o nome da chave
    choskey = input("Qual chave gostaria de alterar: ").strip().lower()
    if choskey: #NOTE - Esta verificando se choskey tem um valor atribuido
        #Informar novo valor
            usuario[choskey] = input("Novo valor: ").strip()
            continue
    else:
         break