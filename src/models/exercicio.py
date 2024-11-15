class Exercicio:
    def __init__(self, nome: str, equipamento: str, repeticoes: int,
                 series: int):
        self.nome = nome
        self.equipamento = equipamento
        self.repeticoes = repeticoes
        self.series = series

    def exibir_detalhes(self):
        return (f"{self.nome} (Equipamento: {self.equipamento}, "
                f"Repetições: {self.repeticoes}, Séries: {self.series})")
