from utils.file_utils import list_audios, extract_ids
from repository.atendimento_repository import search_info_costumers
from utils.csv_utils import save_csv

def build_metadata(pasta_entrada, pasta_saida):
    arquivos = list_audios(pasta_entrada)
    ids = extract_ids(arquivos)
    dados = search_info_costumers(ids)
    save_csv(dados, pasta_saida)
