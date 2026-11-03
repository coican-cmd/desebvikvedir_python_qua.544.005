# classe
classe Pessoa:
def __init__(self,nome,idade,cpf,telefone,email):
    self.__nome = nome
    self.__idade = idade
    self.__cpf = cpf
    self.__telefone = telefone
    self.__email = email

    # métodos set e get
    @property
    def nome(self):
        return self.__nome