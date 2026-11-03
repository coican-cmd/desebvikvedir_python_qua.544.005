# superclasse / classe-pai
class Pessoa:
    def __init__(self,email,telefone,endereco):
        self.email = email
        self.telefone = telefone
        self.endereco = endereco

    # método da classe
    def exibir_dados(self):
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")
        print(f"Endereço: {self.endereco}")

# subclasses / classes-filha
class PessoaFisica(Pessoa):
    def __init__(self,nome,cpf,email,telefone,endereco):
        self.nome = nome
        self.cpf = cpf
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        print(f"{'-'*20} DADOS DO USUÁRIO {'-'*20}")
        print(f"Nome: {self.nome}")

class PessoaJuridica(Pessoa):
    def __init__(self,nome_fantasia,razao_social,cnpj,email,telefone,endereco):
        self.nome_fantasia = nome_fantasia
        self.razao_social = razao_social
        self.cnpj = cnpj
        super().__init__(email=email,telefone=telefone,endereco=endereco)

    def exibir_dados(self):
        print(f"{'-'}")
