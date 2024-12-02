class PlanoContrato:
    def __init__(self, tipo, valor_mensal, duracao_meses):
        self.tipo = tipo
        self.valor_mensal = valor_mensal
        self.duracao_meses = duracao_meses

    def calcular_valor_total(self):
        return self.valor_mensal * self.duracao_meses

    def exibir_detalhes_plano(self):
        return (f"Plano: {self.tipo}, Valor Mensal: R${self.valor_mensal:.2f},"
                f" Duração: {self.duracao_meses} meses")
