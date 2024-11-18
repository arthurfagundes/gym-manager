from src.models.aluno import Aluno
from src.models.plano_contato import PlanoContrato
from src.models.treinador import Treinador
from src.models.treino import Treino
from src.models.exercicio import Exercicio
from src.views.menu import (
    exibir_menu,
    obter_opcao_usuario,
    cadastrar_aluno,
    cadastrar_treinador,
    cadastrar_plano,
    escolher_aluno,
    escolher_treino,
    exibir_alunos,
    exibir_planos,
    exibir_treinador,
    exibir_treinos_aluno
)


def main():
    alunos = []
    treinadores = []
    planos = []

    while True:
        exibir_menu()
        opcao = obter_opcao_usuario()
        if opcao == '1':
            dados_aluno = cadastrar_aluno()
            if dados_aluno:
                (nome, idade, email, tipo_plano, valor_mensal,
                 duracao_meses) = dados_aluno
                plano_contrato = PlanoContrato(tipo_plano, valor_mensal,
                                               duracao_meses)
                aluno = Aluno(nome, idade, email, plano_contrato)
                alunos.append(aluno)
        elif opcao == '2':
            dados_treinador = cadastrar_treinador()
            if dados_treinador:
                nome, idade, email, especialidade = dados_treinador
                treinador = Treinador(nome, idade, email, especialidade)
                treinadores.append(treinador)
                print("Treinador cadastrado com sucesso!")
        elif opcao == '3':
            dados_plano = cadastrar_plano()
            if dados_plano:
                tipo_plano, valor_mensal, duracao_meses = dados_plano
                plano_contrato = PlanoContrato(tipo_plano, valor_mensal,
                                               duracao_meses)
                planos.append(plano_contrato)
                print("Plano de contrato cadastrado com sucesso!")
        elif opcao == '4':
            aluno_selecionado = escolher_aluno(alunos)
            if aluno_selecionado:
                nome_treino = input("Nome do Treino: ")
                nivel_dificuldade = input("Nível de Dificuldade: ")
                treino = Treino(nome_treino, nivel_dificuldade)
                aluno_selecionado.adicionar_treino(treino)
                print(f"Treino '{nome_treino}' adicionado ao "
                      f"aluno {aluno_selecionado.nome}.")
        elif opcao == '5':
            aluno_selecionado = escolher_aluno(alunos)
            if aluno_selecionado:
                treino_selecionado = escolher_treino(aluno_selecionado)
                if treino_selecionado:
                    nome_exercicio = input("Nome do Exercício: ")
                    equipamento = input("Equipamento: ")
                    repeticoes = int(input("Repetições: "))
                    series = int(input("Séries: "))
                    exercicio = Exercicio(nome_exercicio, equipamento,
                                          repeticoes, series)
                    treino_selecionado.adicionar_exercicio(exercicio)
                    print(
                        f"Exercício '{nome_exercicio}' adicionado "
                        f"ao treino '{treino_selecionado.nome}'.")
        elif opcao == '6':
            exibir_alunos(alunos)
        elif opcao == '7':
            exibir_treinador(treinadores)
        elif opcao == '8':
            aluno_selecionado = escolher_aluno(alunos)
            if aluno_selecionado:
                exibir_treinos_aluno(aluno_selecionado)
        elif opcao == '9':
            exibir_planos(planos)
        elif opcao == '10':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

