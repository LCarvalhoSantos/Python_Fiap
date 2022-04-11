equip = []
valor = []
serial = []
depto = []

resposta = "S"

#USANDO APPEND PARA POPULAR LISTAS ORDENADAS 
while resposta == "S":
    equip.append(input("Equipamento: ").upper())
    valor.append(float(input("Valor: ")))
    serial.append(int(input("Digite o número Serial: ")))
    depto.append(input("Departamento: "))
    resposta = (input("Para continuar inserindo equipamentos digite 'S': \n")).upper()

#EXIBINDO DADOS DOS ITENS
for indice in range(0,len(equip)):
    print("----------------------")
    print("Item: ")
    print("Equipamento: " , equip[indice])
    print("Valor: ", valor[indice])
    print("Serial: ", serial[indice])
    print("Valor: ", depto[indice])
    print("----------------------")

#BUSCANDO DADOS INSERIDOS
busca=input("Digite o nome do equipamento que deseja buscar: ").upper()
for indice in range(0,len(equip)):
  if busca==equip[indice]:
    print("Valor: ", valor[indice])
    print("Serial: ", serial[indice])