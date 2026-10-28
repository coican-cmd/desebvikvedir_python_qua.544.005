# biblioteca
import os


# funções
def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def bias_vindas(nome):
    return f"{nome}, seja bem vindo!"


# algoritimo principal
limpar()
nome = input("Informe seu nome: ").strip().title()
print(noas_vindas(nome))