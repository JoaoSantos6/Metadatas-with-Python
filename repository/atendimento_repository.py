from config.db_config import get_connection
from model.costumer import Costumer

def search_info_costumers(lista_ids):
    conn = get_connection()
    cursor = conn.cursor()

    clientes = []
    for id_atendimento in lista_ids:
        cursor.execute("""
            SELECT nome, cpf, telefone, data_nascimento
            FROM clientes
            WHERE atendimento_id = %s
        """, (id_atendimento,))
        row = cursor.fetchone()
        if row:
            cliente = Costumer(
                id_atendimento=id_atendimento,
                nome=row[0],
                cpf=row[1],
                telefone=row[2],
                data_nascimento=row[3]
            )
            clientes.append(cliente)

    conn.close()
    return clientes
