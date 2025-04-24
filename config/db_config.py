from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()  # Carrega variáveis do arquivo .env

def get_connection():
    return psycopg2.connect(
        host     = os.environ['DATASOURCE_HOST'],
        dbname   = os.environ['DATASOURCE_DB'],
        user     = os.environ['DATASOURCE_USER'],
        password = os.environ['DATASOURCE_PASSWORD']
    )
