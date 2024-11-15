class Treino:
    def __init__(self, nome: str, nivel_dificuldade: str):
        self.nome = nome
        self.nivel_dificuldade = nivel_dificuldade
        self.exercicios = []

    def adicionar_exercicio(self, exercicio):
        self.exercicios.append(exercicio)

    def exibir_treino(self):
        exercicios_info = ', '.join([exercicio.exibir_detalhes()
                                     for exercicio in self.exercicios])
        return (f"Treino: {self.nome}, Nível de Dificuldade: "
                f"{self.nivel_dificuldade}, Exercícios: [{exercicios_info}]")
