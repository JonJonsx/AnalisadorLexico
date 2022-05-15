NUMERO = "0123456789"

LETRAS = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

lista = ["t", "e", "x", "t", "o", ";", "1", "3",
         "7", "8", ";", "t", "e", "x", "t", "o", "4", "6"]

numero_completo = []
resultado = []
for index, i in enumerate(lista):
    if i in NUMERO:

        if index == len(lista)-1:
            numero_completo.append(i)
            resultado.append([float("".join(numero_completo)), 3])
            numero_completo = []
            break
        elif lista[index+1] in NUMERO:
            numero_completo.append(i)
        else:
            numero_completo.append(i)
            resultado.append([float("".join(numero_completo)), 3])
            numero_completo = []

for i in resultado:
    print(i)
