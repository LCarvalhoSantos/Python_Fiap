#CRIANDO ARQUIVO TXT
with open("teste.txt","w") as arquivo:
    arquivo.write("Fácil, fácil criar um arquivo.")
#ADICIONANDO TEXTO COM METODO APPEND
with open("teste.txt","a") as arquivo:
    arquivo.write("Continuação do texto.")