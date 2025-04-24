from threading import Thread
from queue import Queue
from time import sleep
from model.costumer import Costumer

from config.db_config import get_connection
from config.threads_config import ThreadsConfig

def worker(queue_ids, queue_resultado):
    conn = get_connection()
    cursor = conn.cursor()
    resultados = []

    while not queue_ids.empty():
        try:
            id_atendimento = queue_ids.get_nowait()
        except:
            break

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

        sleep(5)  # simula latência

        if row:
            cliente = Costumer(
                id_call=id_atendimento,
                name=row[0],
                document=row[1],
                phone=row[2],
                tipo=row[3],
                duracao=row[4]
            )
            resultados.append(cliente)

        queue_ids.task_done()

    conn.close()
    queue_resultado.put(resultados)

def search_info_costumers(lista_ids):
    queue_ids = Queue()
    queue_resultado = Queue()

    threads_config = ThreadsConfig()
    num_threads = threads_config.threads_default

    for id_ in lista_ids:
        queue_ids.put(id_)

    threads = []
    for _ in range(num_threads):
        t = Thread(target=worker, args=(queue_ids, queue_resultado))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    todos_clientes = []
    while not queue_resultado.empty():
        todos_clientes.extend(queue_resultado.get())

    return todos_clientes
