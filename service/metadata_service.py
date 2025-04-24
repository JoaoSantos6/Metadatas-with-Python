from utils.file_utils import list_audios, extract_ids
from repository.atendimento_repository import search_info_costumers
from utils.csv_utils import save_csv

def build_metadata(path_entry, path_output):

    arquivos = list_audios(path_entry)
    print(f"Arquivos encontrados: {arquivos}")

    ids = extract_ids(arquivos)
    print(f"IDs encontrados: {ids}")

    exit('debbuging')

    dados = search_info_costumers(ids)
    save_csv(dados, path_output)
