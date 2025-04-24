import os
import csv

def save_csv(dados, path_output):
    directory = os.path.dirname(path_output)
    if not os.path.exists(directory):
        os.makedirs(directory)

    dados_dict = [cliente.to_dict() for cliente in dados]

    with open(path_output, 'w', newline='') as f:
        fieldnames = ['id_call', 'name', 'document', 'phone', 'tipo', 'duracao']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writeheader()  
        writer.writerows(dados_dict)  
