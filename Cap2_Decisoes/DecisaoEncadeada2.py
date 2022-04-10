nome = input("Nome: ")
idade = int(input("Idade:"))
doenca = input("Possui doença contagiosa: ").upper()

#DESCOBRINDO O PRIMEIRO PROBLEMA
if doenca=="SIM":
    print("SALA AMARELA")
elif doenca=="NAO":
    print("SALA BRANCA")
else:
    print("Responda o campo de doença contagiosa com 'SIM' ou 'NAO'")

#USANDO OUTROS MEIOS DE DEFINIR PRIORIDADE
if idade>=65:
    print("COM PRIORIDADE")
elif idade<65:
    genero = input("Genero: ").upper()
    if genero=="FEMININO" and idade>=10:
        gravidez = input("Está gestante: ").upper()
        if gravidez=="SIM":
            print("COM PRIORIDADE")
        elif gravidez=="NAO":
            print("SEM PRIORIDADE")
        else:
            print("PREENCHA CAMPO DE GRAVIDEZ COM 'SIM' E 'NAO'!")
    elif genero=="FEMININO" and idade<10:
        print("SEM PRIORIDADE")
    elif genero=="MASCULINO":
        print("SEM PRIORIDADE")
    else:
        print("PREENCHA O CAMPO DE GENERO COM 'MASCULINO' E 'FEMININO'!")