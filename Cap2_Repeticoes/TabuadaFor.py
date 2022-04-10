num = int(input("Numero: "))
print("Tabuada do " + str(num)+":")
#UTILIZAÇÃO DO LAÇO DE REPETIÇÃO PARA EXECUTAR A TABUADA
for teste in range(1,11,1):
    print(str(num) + " x "+ str(teste) + " = " + str(num*teste))