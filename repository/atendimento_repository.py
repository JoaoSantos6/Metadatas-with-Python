from time import sleep
from config.db_config import get_connection
from model.costumer import Costumer

def search_info_costumers(lista_ids):
    conn = get_connection()
    cursor = conn.cursor()

    clientes = []
    for id_atendimento in lista_ids:
        cursor.execute("""
            SELECT 
                       nome_cli, 
                       document_cli, 
                       phone_cli, 
                       tipo_atendimento,
                       duracao
            FROM call_info
            WHERE id_call = %s
        """, (id_atendimento,))
        row = cursor.fetchone()

        sleep(5) #simula latencia em ambiente produtivo

        if row:
            cliente = Costumer(
                id_call=id_atendimento,
                name=row[0],
                document=row[1],
                phone=row[2],
                tipo=row[3],
                duracao=row[4]
            )
            clientes.append(cliente)

    conn.close()
    return clientes
