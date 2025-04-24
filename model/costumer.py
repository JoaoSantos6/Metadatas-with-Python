from dataclasses import dataclass

@dataclass
class Costumer:
    id_call: str
    name: str
    document: str
    phone: str
    tipo: str
    duracao: str

    def to_dict(self):
        return {
            'id_call': self.id_call,
            'name': self.name,
            'document': self.document,
            'phone': self.phone,
            'tipo': self.tipo,
            'duracao': self.duracao
        }
