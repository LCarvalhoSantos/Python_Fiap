#RECEBE A QUANTIDADE DE PACIENTES
pacientes = int(input("Pacientes: "))
paci = int(1)

while paci <= pacientes and pacientes != 0:
    nome = input("Nome: ")
    idade = int(input("Idade:"))
    doenca = input("Possui doença contagiosa: ").upper()

#USANDO LAÇO DE REPETIÇÃO PARA OBTER A RESPOSTA CORRETA
    while doenca != "SIM" and doenca != "NAO":
        print("Digite 'SIM' ou 'NAO'")
        doenca = input("Possui doença contagiosa: ").upper()
    if doenca == "SIM":
        print("SALA AMARELA")
    else:
        print("SALA BRANCA")

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
        print("================================================")

#INCREMENTANDO O CONTADOR
    paci+=1   