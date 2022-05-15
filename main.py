
import ler_csv as ler
import operadores as op
import tokeniza as tk

PROMPT = "expressão >>> "
QUIT = ''

# ------------------------------------------------------------


def perguntar_arquivo():
    opcao = input("Quer ler um arquivo? (S/N) ")
    expressao = ""
    if opcao.upper() == "S":
        arquivo = input("Digite o caminho do arquivo >>> ")
        expressao = ler.ler_arquivo_csv(arquivo)
    else:
        print("Entre como uma expressão ou tecle apenas ENTER para encerrar.")
        PROMPT = "expressão >>> "
        expressao = input(PROMPT)

    return expressao


def main():
    expressao = perguntar_arquivo()
    while expressao != QUIT:
        lista_tokens = tk.tokeniza(expressao)
        for token in lista_tokens:
            # pegue item e tipo
            item, tipo = token

            # cri string com a descriçao
            if tipo in [tk.OPERADOR, tk.PARENTESES]:
                descricao = "'%s' : %s" % (item, op.DESCRICAO[item])
            elif tipo == tk.VARIAVEL:
                descricao = "'%s' : nome de variável" % item
            elif tipo == tk.NUMERO:
                descricao = "%f : constante float" % item
            elif tipo == tk.SEPARADOR:
                descricao = "'%s' : separador" % item
            else:
                descricao = "'%s' : categoria desconhecida" % item

            # imprima a descriçao
            print(descricao)

        # leia próxima expressão
        expressao = perguntar_arquivo()


# -------------------------------------------
# início da execução do programa
main()
