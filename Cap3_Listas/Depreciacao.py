impressora = []
serial = []
valor = []

resposta = "S"
depreciacao = float(input("Depreciação: "))

#CADASTRANDO IMPRESSORAS
while resposta == "S":
    impressora.append(input("Impressora: "))
    valor.append(float(input("Valor: ")))
    serial.append(int(input("Serial: ")))
    resposta = input("Para inserir mais equipamentos digite 'S': \n ").upper()

#EXIBINDO IMPRESSORAS CADASTRADAS
for indice in range(0,len(impressora)):
    print("------------IMPRESSORA "+ str(impressora[indice]) +"------------")
    print("impressora:........... "+ impressora[indice])
    print("Serial:............ " + str(serial[indice]))
    print("Valor:........... " + str(valor[indice]) + "\n")

#DEPRECIANDO VALOR DA IMPRESSORA
for indice in range(0,len(impressora)):
    valor[indice] = valor[indice] * (1-(depreciacao / 100))
    print("A impressora: "+ impressora[indice] + " sofreu uma depreciação de "+ str(depreciacao) + "%.")
    print("Valor atual: " + str(valor[indice]) + "\n")
    print("------------IMPRESSORA "+ str(impressora[indice]) +"------------")


