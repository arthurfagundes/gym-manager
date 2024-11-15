from .pessoa import Pessoa
from .plano_contato import PlanoContrato


class Aluno(Pessoa):
    def __init__(self, nome, idade, email, plano_contrato):
        super().__init__(nome, idade, email)
        self.plano_contrato = plano_contrato
        self.status_pagamento = False
        self.treinos = []

    def adicionar_treino(self, treino):
        self.treinos.append(treino)

    def verificar_status_pagamento(self) -> bool:
        return self.status_pagamento

    def exibir_informacoes(self):
        info = super().exibir_informacoes()
        return (f"{info}, {self.plano_contrato.exibir_detalhes_plano()}"
                f", Status de Pagamento: "
                f"{'PAGO' if self.status_pagamento else 'PENDENTE'}")
