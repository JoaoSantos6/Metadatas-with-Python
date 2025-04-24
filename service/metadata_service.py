from utils.file_utils import list_audios, extract_ids
from repository.atendimento_repository import search_info_costumers
from utils.csv_utils import save_csv

def build_metadata(path_entry, path_output):

    arquivos = list_audios(path_entry)
    print(f"\nArquivos encontrados: {arquivos}")

    ids = extract_ids(arquivos)
    print(f"\nIDs encontrados: {ids}")

    dados = search_info_costumers(ids)
    print(f"\nDados encontrados: {dados}")

    save_csv(dados, path_output)
