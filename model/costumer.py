from dataclasses import dataclass

@dataclass
class Costumer:
    id_call: str
    name: str
    document: str
    phone: str
    date_call: str  # ou datetime.date, se quiser validar datas
