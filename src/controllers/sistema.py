from src.models.aluno import Aluno
from src.models.plano_contrato import PlanoContrato
from src.models.treinador import Treinador
from src.models.treino import Treino
from src.models.exercicio import Exercicio
from src.utils.helpers import obter_numero_inteiro
from src.views.menu import (
    exibir_menu,
    obter_opcao_usuario,
    cadastrar_aluno,
    cadastrar_treinador,
    escolher_aluno,
    escolher_treino,
    exibir_alunos,
    exibir_treinador,
    exibir_treinos_aluno
)


def main(planos):
    alunos = []
    treinadores = []

    while True:
        exibir_menu()
        opcao = obter_opcao_usuario()
        if opcao == 1:
            dados_aluno = cadastrar_aluno(planos)
            if dados_aluno:
                nome, idade, email, plano_contrato = dados_aluno
                aluno = Aluno(nome, idade, email, plano_contrato)
                alunos.append(aluno)
                print(f"Aluno {nome} cadastrado com sucesso!")
        elif opcao == 2:
            dados_treinador = cadastrar_treinador()
            if dados_treinador:
                nome, idade, email, especialidade = dados_treinador
                treinador = Treinador(nome, idade, email, especialidade)
                treinadores.append(treinador)
                print("Treinador cadastrado com sucesso!")
        elif opcao == 3:
            aluno_selecionado = escolher_aluno(alunos)
            if aluno_selecionado:
                nome_treino = input("Nome do Treino: ")
                nivel_dificuldade = input("Nível de Dificuldade: ")
                treino = Treino(nome_treino, nivel_dificuldade)
                aluno_selecionado.adicionar_treino(treino)
                print(f"Treino '{nome_treino}' adicionado ao aluno {aluno_selecionado.nome}.")
        elif opcao == 4:
            aluno_selecionado = escolher_aluno(alunos)
            if aluno_selecionado:
                treino_selecionado = escolher_treino(aluno_selecionado)
                if treino_selecionado:
                    nome_exercicio = input("Nome do Exercício: ")
                    equipamento = input("Equipamento: ")
                    repeticoes = obter_numero_inteiro("Repetições: ")
                    series = obter_numero_inteiro("Séries: ")
                    exercicio = Exercicio(nome_exercicio, equipamento, repeticoes, series)
                    treino_selecionado.adicionar_exercicio(exercicio)
                    print(f"Exercício '{nome_exercicio}' adicionado ao treino '{treino_selecionado.nome}'.")

        elif opcao == 5:
            exibir_alunos(alunos)
        elif opcao == 6:
            exibir_treinador(treinadores)
        elif opcao == 7:
            aluno_selecionado = escolher_aluno(alunos)
            if aluno_selecionado:
                exibir_treinos_aluno(aluno_selecionado)
        elif opcao == 8:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")
