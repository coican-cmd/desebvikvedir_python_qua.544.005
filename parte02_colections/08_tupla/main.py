#NOTE - Não tem nada haver com Tupla do banco de dados

#NOTE - É uma lista IMUTAVEL, que serve apenas pra exibição

#NOTE - Diferente da lista que é escrita com [], esta é escrita com ()

dotw = (
    "Domingo",
    "Segunda-Feira",
    "Terça-Feira",
    "Quarta-Feira",
    "Quinta-Feira",
    "Sexta-Feira",
    "Sábado",
)

print("")

# Exibe a tupla
for day in dotw:
    print(f'{day}')

#NOTE - Caso tentem alterar a tupla, o programa dara erro. Exemplo:

try:
    dotw.sort()
    for day in dotw:
        print(day)
except Exception as e:
    print(f"Algo deu errado!!!\n\nERROR {e}")
finally:
    print("Programa encerrado")