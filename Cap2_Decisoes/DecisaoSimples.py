nome = input("Nome: ")
idade = int(input("Idade: "))
priorid = "Não"
if idade >= 65:
    priorid = "Sim"
print("O paciente " + nome + " possui atendimento prioritário? " + priorid)

