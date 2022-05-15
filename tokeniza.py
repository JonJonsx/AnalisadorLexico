# Constantes
TESTE = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="
# [\%\*\/\+\-\!\^\=]

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."
PONTO_E_VIRGULA = ";"
# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"

OPERADOR = 1  # para operadores aritméticos e atribuição
NUMERO = 2  # para números: todos são considerados float
VARIAVEL = 3  # para variáveisss
PARENTESES = 4  # para '(' e ')
SEPARADOR = 5

BRANCOS = [' ', '\n', '\t', '\v', '\f', '\r']
COMENTARIO = "#"

# media_prova = (p1 + p2) #/2
# ------------------------------------------------------------


def tokeniza(exp):
    resultado = []
    variavel_sep = []
    numero_completo = []
    for index, i in enumerate(exp):
        if i in COMENTARIO:
            break
        if i in LETRAS:
            variavel_sep.append(i)
            if exp[index+1] in DIGITOS:
                variavel_sep.append(exp[index+1])
            if exp[index+1] not in LETRAS:
                variavel_com = ''.join(variavel_sep)
                resultado.append([variavel_com, VARIAVEL])
                variavel_sep = []
        elif i in OPERADORES:
            resultado.append([i, OPERADOR])
        elif i in ABRE_FECHA_PARENTESES:
            resultado.append([i, PARENTESES])
        elif i in PONTO_E_VIRGULA:
            resultado.append([i, SEPARADOR])
        elif i in DIGITOS:
            if exp[index-1] not in LETRAS:
                if index == len(exp) - 1:
                    numero_completo.append(i)
                    resultado.append([float("".join(numero_completo)), NUMERO])
                    numero_completo = []
                elif exp[index+1] in DIGITOS:
                    numero_completo.append(i)
                else:
                    numero_completo.append(i)
                    resultado.append([float("".join(numero_completo)), NUMERO])
                    numero_completo = []

            # if exp[index-1] not in LETRAS:
            #     resultado.append([float(i), NUMERO])
    return resultado
