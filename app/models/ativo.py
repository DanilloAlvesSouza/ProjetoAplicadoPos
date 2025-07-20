class Ativo:
    def __init__(self, nome, vencimento, ultimo_preco):
        self.nome = nome
        self.vencimento = vencimento
        self.ultimo_preco = ultimo_preco

    def to_dict(self):
        return {
            "Nome": self.nome,
            "Vencimento": str(self.vencimento),
            "Ultimo_Preco": self.ultimo_preco
        }
