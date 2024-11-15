class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_informacoes(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}"
