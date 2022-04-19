from Funcoes import *
users = {}

res = per()

while res == "I" or res == "P" or res == "E" or res == "L" or res == "S":
    if res == "I":
        entrada(users)
        res = per()

