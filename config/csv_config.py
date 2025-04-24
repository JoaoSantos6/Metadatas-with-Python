class CsvConfig:
    def __init__(self, delimiter: str = ',', quotechar: str = '"'):
        self.file_path = "C:/Projetos/Metadados/relatorios/"
        self.name = 'metadatas_{yyyymmdd}.csv'
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.fieldnames = ['id_call', 'name', 'document', 'phone', 'tipo', 'duracao']