import os
import re

def list_audios(caminho):
    return [f for f in os.listdir(caminho) if f.endswith(".mp3") or f.endswith(".wav")]

def extract_ids(arquivos):
    ids = []
    for arquivo in arquivos:
        match = re.search(r"(\d+)", arquivo)
        if match:
            ids.append(match.group(1))
    return ids
