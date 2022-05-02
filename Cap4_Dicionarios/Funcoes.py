from datetime import datetime

data = datetime.now()

#PERGUNTAS PARA ENTRADA DE DADOS
def per():
    res = input("Digite: I = Inserir, P = Pesquisar, E = Excluir, L = Listar ou S = Sair: ").upper()
    return str(res)
#GUARDANDO DADOS NO DICIONARIO

def entrada(dic):
    dic[int(input("Digite o código do usuário: "))]=[input("Nome: "), input("Data de ultimo acesso: "), input("Nivel de acesso: "), data]

#PESQUISANDO LOGINS
def pesquisar(dic, cod):
    codigo = dic.get(cod)
    if codigo != None:
        print("Nome: " + codigo[0])
        print("Data: " + codigo[1])

#EXCLUIR ITENS DO DICIONARIO
def excluir(dic, cod):
    if dic.get(cod)!=None:
        del dic[cod]    
    return "Excluído"

#EXIBINDO DICIONARIO
def listar(dic):
    print(dic)