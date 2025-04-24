from service.metadata_service import build_metadata
from pathlib import Path
import os
from os import environ
from config.audio_config import AudioConfig

if __name__ == "__main__":

    audio_config = AudioConfig()

    pasta_audios = os.environ['AUDIO_PATH'] if 'AUDIO_PATH' in os.environ else "audios/"
    pasta_destino = audio_config.audio_dir

    build_metadata(pasta_audios, pasta_destino)
    print("Relatório gerado com sucesso!")