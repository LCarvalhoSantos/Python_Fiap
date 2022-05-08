def chamarMenu():
    escolha = int(input("Digite: \n 1 - Registrar ativo \n 2 - Persistir em arquivo \n 3 - Exibir ativos armazenados: "))
    return escolha

def registrar(dicionario):
    resp="S"
    while resp=="S":
        dicionario[input("Digite o número patrimonial: ")]=[
        input("Data da última atualização: "),
        input("Descrição: "),
        input("Departamento: ")]
        resp=input("Digite 'S' para continuar.").upper()

def persistir(dicionario):
    with open("inventario.csv", "a") as inv:
        for chave, valor in dicionario.items():
            inv.write(chave + ";" + valor[0] + ";" + valor[1] + ";" + valor[2] + "\n")
    return "Persistido com sucesso"

def exibir():
    with open("inventario.csv", "r") as inv:
        linhas=inv.readlines()
    return linhas