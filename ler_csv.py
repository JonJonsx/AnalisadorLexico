import csv


def ler_arquivo_csv(caminho_arquivo):
    try:
        with open(str(caminho_arquivo), "r", encoding="utf-8", newline="") as fid:
            reader = csv.reader(fid, delimiter=";")
            lista = []
            for row in reader:
                for i in row:
                    lista.append(i)

            csv_convertido = ";".join(lista)
            return str(csv_convertido)
    except:
        print("Não foi possivel ler o arquivo")
