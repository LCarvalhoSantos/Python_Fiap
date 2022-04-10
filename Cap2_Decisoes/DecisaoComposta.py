nome=input("Digite o nome: ")
idade=int(input("Digite a idade: "))
doenca=input("Doença contagiosa: ").upper()
if idade>=65 and doenca=="SIM":
    print("Paciente: " + nome + " | SALA AMARELA - COM PRIORIDADE ")
elif idade<65 and doenca=="SIM":
    print("Paciente: " + nome + " | SALA AMARELA - SEM PRIORIDADE")
elif idade>=65 and doenca=="NAO":
    print("Paciente: "+nome+" | SALA BRANCA - COM PRIORIDADE")
elif idade<65 and doenca=="NAO":
    print("Paciente: "+nome+" | SALA BRANCA - SEM PRIORIDADE")
else:
    print("Preencha o campo 'Doença contagiosa' com SIM e Nao!")