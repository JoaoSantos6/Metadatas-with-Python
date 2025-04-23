import csv
import os

def save_csv(dados, pasta_saida):
    os.makedirs(pasta_saida, exist_ok=True)
    caminho = os.path.join(pasta_saida, "metadados.csv")
    with open(caminho, mode='w', newline='', encoding='utf-8') as arquivo:
        writer = csv.DictWriter(arquivo, fieldnames=["id", "nome", "cpf", "telefone"])
        writer.writeheader()
        writer.writerows(dados)
