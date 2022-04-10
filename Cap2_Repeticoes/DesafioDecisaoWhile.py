print("Defina seu nível de acesso: ADM para administradores, USR para usuários ou GST para visitantes; e insira seu genero")
nivel = input("Nível: ").upper()
genero = input("Genero: ").upper()
resposta = "SIM"
while resposta == "SIM":
    if genero=="MASCULINO":
        if nivel == "ADM":
            print("Olá Administrador!")
        elif nivel == "USR":
            print("Olá Usuário!")
        elif nivel == "GST":
            print("Olá Visitante!")
        else:
            print("Olá Desconhecido!")
    elif genero=="FEMININO":
        if nivel == "ADM":
            print("Olá Administradora!")
        elif nivel == "USR":
            print("Olá Usuária!")
        elif nivel == "GST":
            print("Olá Visitante!")
        else:
            print("Olá Desconhecido!")
    else:
        print("Digite um genero válido!")
    resposta = input("Digite 'SIM' para continuar: ")