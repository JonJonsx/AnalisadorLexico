import csv

with open('./arquivos/teste.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print(";".join(row).replace('"', ''))
