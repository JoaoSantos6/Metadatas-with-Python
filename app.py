from service.metadata_service import build_metadata
from pathlib import Path
import os
from dotenv import load_dotenv
load_dotenv()  # Carrega variáveis do arquivo .env
from config.csv_config import CsvConfig

if __name__ == "__main__":

    csv_config = CsvConfig()


    pasta_audios = os.environ['AUDIO_PATH'] if 'AUDIO_PATH' in os.environ else "audios/"
    pasta_destino = csv_config.file_path + csv_config.name.replace("{yyyymmdd}", "20231010")

    build_metadata(pasta_audios, pasta_destino)
    print("Relatório gerado com sucesso!")