nome = input("Nome: ")
idade = int(input("Idade: "))
doenca = input("Possui doença contagiosa: ").upper()

if idade>=65:
    print("Atendimento COM PRIORIDADE!")
    if doenca=="SIM":
        print("SALA AMARELA!")
    elif doenca=="NAO":
        print("SALA BRANCA")
    else:
        print("Responda o campo de doença contagiosa com 'SIM' ou 'NAO'")

elif idade<65:
    print("Atendimento SEM PRIORIDADE")
    if doenca=="SIM":
        print("SALA AMARELA!")
    elif doenca=="NAO":
        print("SALA BRANCA")
    else:
        print("Responda o campo de doença contagiosa com 'SIM' ou 'NAO'")

    