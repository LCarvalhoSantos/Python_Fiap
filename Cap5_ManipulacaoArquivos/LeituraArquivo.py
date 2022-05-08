#USANDO O READ
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.read()
print("Tipo de dado da variável ", type(conteudo))
print("Conteudo do arquivo: ",conteudo)
#USANDO O READLINES
with open("teste.txt", "r") as arquivo:
    conteudo = arquivo.readlines()
print("Tipo de dado da variável ", type(conteudo))
print("Conteudo do arquivo: ",conteudo)