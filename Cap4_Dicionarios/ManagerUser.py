#IMPORTANDO TODAS AS FUNÇÕES DO ARQUIVO
from Funcoes.Funcoes_Dicionarios import *
users = {}

res = per()

while res == "I" or res == "P" or res == "E" or res == "L" or res == "S":
    
#INCLUINDO USUÁRIOS
    if res == "I":
        entrada(users)
        res = per()
#PESQUISANDO USUARIOS
    elif res == "P":
        pesquisar(users, input("Codigo a ser utilizado: "))
        res = per()
#EXCLUINDO USUARIOS
    elif res == "E":
        excluir(users, input("Codigo a ser excluido: "))
        res = per()
#LISTANDO USUARIOS
    elif res == "L":
        listar(users)
        res = per()
    else:
        break
