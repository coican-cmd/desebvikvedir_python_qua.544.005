# TODO: parte 02 atividade 01
"""
Crie um programa que faça as seguintes operações:
- Cadastra novo usuário (nome, email, telefone, cpf)
- Lista todos os usuários cadastrados
- Altera os dados de um usuário
- Exclui um usuário
- Grava os dados de todos os usuários em um .json
- Abre arquivo .json e lista todos os usuários cadastrados nele
"""

import json

usuarios = []


def cadastrar():
    nome = input("Nome: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cpf = input("CPF: ")

    usuario = {"nome": nome, "email": email, "telefone": telefone, "cpf": cpf}
    usuarios.append(usuario)
    print("Usuário cadastrado!")


def listar():
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado.")
    else:
        for i in range(len(usuarios)):
            u = usuarios[i]
            print(i + 1, "-", u["nome"], "|", u["email"], "|", u["telefone"], "|", u["cpf"])


def alterar():
    listar()
    if len(usuarios) == 0:
        return
    numero = int(input("Número do usuário que deseja alterar: "))
    if numero < 1 or numero > len(usuarios):
        print("Número inválido.")
        return

    u = usuarios[numero - 1]
    u["nome"] = input("Novo nome: ")
    u["email"] = input("Novo email: ")
    u["telefone"] = input("Novo telefone: ")
    u["cpf"] = input("Novo CPF: ")
    print("Usuário alterado!")


def excluir():
    listar()
    if len(usuarios) == 0:
        return
    numero = int(input("Número do usuário que deseja excluir: "))
    if numero < 1 or numero > len(usuarios):
        print("Número inválido.")
        return

    usuarios.pop(numero - 1)
    print("Usuário excluído!")


def salvar_json():
    arquivo = open("Atv01/usuarios.json", "w", encoding="utf-8")
    json.dump(usuarios, arquivo, indent=4, ensure_ascii=False)
    arquivo.close()
    print("Dados salvos em usuarios.json!")


def abrir_json():
    try:
        arquivo = open("Atv01/usuarios.json", "r", encoding="utf-8")
        dados = json.load(arquivo)
        arquivo.close()
    except FileNotFoundError:
        print("Arquivo usuarios.json não encontrado.")
        return

    if len(dados) == 0:
        print("O arquivo está vazio.")
    else:
        for u in dados:
            print(u["nome"], "|", u["email"], "|", u["telefone"], "|", u["cpf"])


while True:
    print()
    print("===== MENU =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Alterar usuário")
    print("4 - Excluir usuário")
    print("5 - Salvar em .json")
    print("6 - Abrir .json e listar")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        salvar_json()
    elif opcao == "6":
        abrir_json()
    elif opcao == "0":
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
