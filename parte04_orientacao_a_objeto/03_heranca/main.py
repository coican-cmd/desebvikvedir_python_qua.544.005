import os

from model import PessoaFisica, PessoaJurídica

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def main():
    # instancia as classes
    usuario = PessoaFisica(nome="",cpf="",email="",telefone="",endereco="")
    empresa = PessoaJuridica(cnpj="",razao_social="",nome_fantasia="",email="",telefone="",endereco="")

    # informa os dados do usuário
    limpar()

    print(f"{'-'*20} Informe os dados do usuário {'-'*20}\n")
    usuario.nome = input("Informe o nome do usuário: ").strip().title()
    usuario.cpf = input("Informe o CPF do usuário: ").strip()
    usuario.email = input("Informe o e-mail do usuário: ").strip().lower()
    usuario.telefone = input("Informe o telefone do usuário: ").strip()
    usuario.endereco = input("Informe o endereço do usuário: ").strip()
    
    # informa os dados da empresa
    limpar()
    print(f"{'-'*20} Informe os dados da empresa {'-'*20}")
    empresa.razao_social = input("Informe a razão social: ").strip()
    empresa.nome_fantasia = input("Informe a nome_fantasia: ").strip().title()
    empresa.cnpj = input("Informe o cnpj: ").strip()
    empresa.email = input("Informe o e-mail: ").strip().lower()
    empresa.telefone = input("Informe o telefone: ").strip()
    empresa.endereco = input("Informe a endereço: ").strip()

if __name__ == "__main__":
    main()