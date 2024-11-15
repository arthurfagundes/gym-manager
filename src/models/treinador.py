from .aluno import Aluno
from .pessoa import Pessoa


class Treinador(Pessoa):
    def __init__(self, nome: str, idade: int, email: str, especialidade: str):
        super().__init__(nome, idade, email)
        self.especialidade = especialidade
        self.alunos = []

    def adicionar_aluno(self, aluno: Aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, aluno: Aluno):
        self.alunos.remove(aluno)

    def criar_plano_treino(self, aluno: Aluno, treino):
        aluno.adicionar_treino(treino)

    def exibir_informacoes(self):
        info = super().exibir_informacoes()
        return f"{info}, Especialidade: {self.especialidade}"
