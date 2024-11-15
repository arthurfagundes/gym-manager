from src.models.aluno import Aluno
from src.models.plano_contato import PlanoContrato
from src.models.treinador import Treinador
from src.models.treino import Treino
from src.models.exercicio import Exercicio


def main():
    alunos = []
    treinadores = []

    while True:
        print("\nMenu:")
        print("1. Cadastrar Aluno")
        print("2. Cadastrar Treinador")
        print("3. Cadastrar Plano de Contrato")
        print("4. Cadastrar Treino")
        print("5. Cadastrar Exercício")
        print("6. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            try:
                nome = input("Nome do Aluno: ")
                idade = int(input("Idade do Aluno: "))
                email = input("Email do Aluno: ")
                tipo_plano = input("Tipo de Plano (Mensal, "
                                   "Trimestral, Anual): ")
                valor_mensal = float(input("Valor Mensal: "))
                duracao_meses = int(input("Duração em Meses: "))
                plano_contrato = PlanoContrato(tipo_plano, valor_mensal,
                                               duracao_meses)
                aluno = Aluno(nome, idade, email, plano_contrato)
                alunos.append(aluno)
                print("Aluno cadastrado com sucesso!")
            except ValueError:
                print("ERRO: Insira um valor válido para idade, "
                      "valor mensal ou duração!")

        elif opcao == '2':
            try:
                nome = input("Nome do Treinador: ")
                idade = int(input("Idade do Treinador: "))
                email = input("Email do Treinador: ")
                especialidade = input("Especialidade do Treinador: ")
                treinador = Treinador(nome, idade, email, especialidade)
                treinadores.append(treinador)
                print("Treinador cadastrado com sucesso!")
            except ValueError:
                print("ERRO: Insira um valor válido para idade!")

        elif opcao == '3':
            try:
                tipo_plano = input("Tipo de Plano (Mensal, "
                                   "Trimestral, Anual): ")
                valor_mensal = float(input("Valor Mensal: "))
                duracao_meses = int(input("Duração em Meses: "))
                plano_contrato = PlanoContrato(tipo_plano, valor_mensal,
                                               duracao_meses)
                print("Plano de contrato cadastrado com sucesso!")
            except ValueError:
                print("ERRO: Insira um valor válido para valor mensal!")

        elif opcao == '4':
            try:
                if not alunos:
                    print("Nenhum aluno cadastrado. "
                          "Cadastre um aluno primeiro.")
                    continue

                print("Alunos cadastrados:")
                for i, aluno in enumerate(alunos):
                    print(f"{i + 1}. {aluno.nome}")

                indice_aluno = int(input("Escolha o número do aluno "
                                         "para adicionar um treino: ")) - 1
                aluno_selecionado = alunos[indice_aluno]

                nome_treino = input("Nome do Treino: ")
                nivel_dificuldade = input("Nível de Dificuldade: ")
                treino = Treino(nome_treino, nivel_dificuldade)

                aluno_selecionado.adicionar_treino(treino)
                print(f"Treino '{nome_treino}' adicionado ao aluno "
                      f"{aluno_selecionado.nome}.")
            except ValueError:
                print("ERRO: Escolha um ID de aluno válido "
                      "para adicionar um treino!")

        elif opcao == '5':
            if not alunos:
                print("Nenhum aluno cadastrado. Cadastre um aluno primeiro.")
                continue

            print("Alunos cadastrados:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            indice_aluno = int(input("Escolha o número do aluno "
                                     "para adicionar um exercício: ")) - 1
            aluno_selecionado = alunos[indice_aluno]

            if not aluno_selecionado.treinos:
                print("Nenhum treino cadastrado para este aluno. "
                      "Cadastre um treino primeiro.")
                continue

            print("Treinos cadastrados:")
            for i, treino in enumerate(aluno_selecionado.treinos):
                print(f"{i + 1}. {treino.nome}")

            indice_treino = int(input("Escolha o número do treino "
                                      "para adicionar um exercício: ")) - 1
            treino_selecionado = aluno_selecionado.treinos[indice_treino]

            nome_exercicio = input("Nome do Exercício: ")
            equipamento = input("Equipamento: ")
            repeticoes = int(input("Repetições: "))
            series = int(input("Séries: "))
            exercicio = Exercicio(nome_exercicio, equipamento,
                                  repeticoes, series)

            treino_selecionado.adicionar_exercicio(exercicio)
            print(f"Exercício '{nome_exercicio}' adicionado ao treino "
                  f"'{treino_selecionado.nome}'.")

        elif opcao == '6':
            print("Saindo do sistema...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
