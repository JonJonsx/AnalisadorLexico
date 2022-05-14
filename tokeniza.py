import re

# Constantes
TESTE = False

# caracteres usados em operadores
OPERADORES = "%*/+-!^="
# [\%\*\/\+\-\!\^\=]

# caracteres usados em números inteiros
DIGITOS = "0123456789"

# ponto decimal
PONTO = "."

# todos os caracteres usados em um números float
FLOATS = DIGITOS + PONTO

# caracteres usados em nomes de variáveis
LETRAS = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
# pega variavel [^\W/][\.a-zA-Z_.\d]+

# abre e fecha parenteses
ABRE_FECHA_PARENTESES = "()"
# [()]

# categorias
OPERADOR = 1  # para operadores aritméticos e atribuição
NUMERO = 2  # para números: todos são considerados float
VARIAVEL = 3  # para variáveisss
PARENTESES = 4  # para '(' e ')

# Whitespace characters: space, newline, horizontal tab,
# vertical tab, form feed, carriage return
BRANCOS = [' ', '\n', '\t', '\v', '\f', '\r']
# espaçoes em branco [^a-zA-Z\+][\\n\\t\\v\\f\\r]
# caractere que indica comentário
COMENTARIO = "#"

# media_prova = (p1 + p2) #/2
# ------------------------------------------------------------


def tokeniza(exp):
    resultado = []
    variavel_sep = []
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
        elif i in DIGITOS:
            if exp[index-1] not in LETRAS:
                resultado.append([float(i), NUMERO])
    return resultado
    """(str) -> lis

    O componente tipo de um token indica a sua categoria
    (ver definição de constantes acima).

        - OPERADOR;
        - NUMERO;
        - VARIAVEL; ou
        - PARENTESES

    A funçao ignora tuo que esta na exp apos o caractere
    COMENTARIO (= "#").
    """
    # escreva o seu código abaixo
