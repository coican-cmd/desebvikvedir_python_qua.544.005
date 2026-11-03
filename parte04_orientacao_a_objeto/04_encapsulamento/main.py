from model import Pessoa


def main():
    usuario = Pessoa(nome="",idade=0,cpf="",email="")

    usuario.nome = input("Informe o nome: ").strip().title

    print(f"Nome: {usuario.nome}")


    if __name__ == "__main__":
        main()