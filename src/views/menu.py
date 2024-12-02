from src.utils.helpers import obter_numero_inteiro


def exibir_menu():
    print("\nMenu:")
    print("1. Cadastrar Aluno")
    print("2. Cadastrar Treinador")
    print("3. Cadastrar Treino")
    print("4. Cadastrar Exercício")
    print("5. Listar Alunos")
    print("6. Listar Treinadores")
    print("7. Listar Treinos de Aluno")
    print("8. Sair")


def obter_opcao_usuario():
    return obter_numero_inteiro(
        "Escolha uma opção (1-8): ",
        "Erro: Opção inválida. Escolha entre 1 e 8.",
        min_valor=1,
        max_valor=8
    )


def cadastrar_aluno(planos):
    try:
        nome = input("Nome do Aluno: ")
        idade = obter_numero_inteiro("Idade do Aluno: ",
                                     "Erro: Idade inválida", min_valor=1)
        email = input("Email do Aluno: ")
        print("Escolha o plano do aluno:")
        for i, plano in enumerate(planos, 1):
            print(f"{i}. {plano.tipo} - R${plano.valor_mensal:.2f} por mês - "
                  f"{plano.duracao_meses} meses")
        opcao_plano = obter_numero_inteiro("Escolha uma opção: ",
                                           "Erro: Escolha uma opção válida.",
                                           min_valor=1,
                                           max_valor=len(planos))
        plano_contrato = planos[opcao_plano - 1]
        return nome, idade, email, plano_contrato
    except ValueError:
        print(
            "ERRO: Insira um valor válido para idade, valor mensal ou duração!")
        return None


def cadastrar_treinador():
    try:
        nome = input("Nome do Treinador: ")
        idade = obter_numero_inteiro("Idade do Treinador: ",
                                     "Erro: Idade inválida.", min_valor=18)
        email = input("Email do Treinador: ")
        especialidade = input("Especialidade do Treinador: ")
        return nome, idade, email, especialidade
    except ValueError:
        print("ERRO: Insira um valor válido para idade!")
        return None


def escolher_aluno(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado. Cadastre um aluno primeiro.")
        return None
    print("Alunos Cadastrados:")
    for i, aluno in enumerate(alunos):
        print(f"{i + 1}. {aluno.nome}")
        indice_aluno = obter_numero_inteiro("Escolha o número do aluno: ",
                                            "Erro: Escolha um número válido.",
                                            min_valor=1,
                                            max_valor=len(alunos))
        return alunos[indice_aluno - 1]


def escolher_treino(aluno):
    if not aluno.treinos:
        print("Nenhum treino cadastrado para este aluno. "
              "Cadastre um treino primeiro.")
        return None
    print("Treinos cadastrados:")
    for i, treino in enumerate(aluno.treinos):
        print(f"{i + 1}. {treino.nome}")
        indice_treino = obter_numero_inteiro("Escolha o número do treino: ",
                                             "Erro: Escolha um número válido.",
                                             min_valor=1,
                                             max_valor=len(aluno.treinos))
        return aluno.treinos[indice_treino - 1]


def exibir_alunos(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    print("\nAlunos Cadastrados:")
    for i, aluno in enumerate(alunos):
        print(f"\n{i + 1}. "
              f"Nome: {aluno.nome} "
              f"\n   Idade: {aluno.idade} "
              f"\n   Email: {aluno.email} "
              f"\n   Plano: {aluno.plano_contrato.tipo} "
              f"\n   Valor Mensal: R${aluno.plano_contrato.valor_mensal:.2f} "
              f"\n   Duração: {aluno.plano_contrato.duracao_meses} meses")


def exibir_treinador(treinadores):
    if not treinadores:
        print("Nenhum treinador cadastrado.")
        return
    print("\nTreinadores Cadastrados:")
    for i, treinador in enumerate(treinadores):
        print(f"\n{i + 1}."
              f"Nome: {treinador.nome} "
              f"\n   Idade: {treinador.idade} "
              f"\n   Email: {treinador.email}"
              f"\n   Especialidade: {treinador.especialidade}")


def exibir_treinos_aluno(aluno):
    if not aluno.treinos:
        print(f"O aluno {aluno.nome} não tem treinos cadastrados.")
        return
    print(f"\nTreinos de {aluno.nome}:")
    for i, treino in enumerate(aluno.treinos):
        print(
            f"\n{i + 1}."
            f"Nome: {treino.nome} "
            f"\n   Nível de Dificuldade: {treino.nivel_dificuldade}")
        if treino.exercicios:
            print("Exercícios: ")
            for exercicio in treino.exercicios:
                print(f"   - {exercicio.exibir_detalhes()}")
        else:
            print("   Nenhum exercício cadastrado neste treino.")


def exibir_planos(planos):
    if not planos:
        print("Nenhum plano cadastrado.")
        return
    print("\nPlanos de Contrato Cadastrados:")
    for i, plano in enumerate(planos):
        print(
            f"\n{i + 1}."
            f"Tipo: {plano.tipo} "
            f"\n   Valor Mensal: R${plano.valor_mensal:.2f}"
            f"\n   Duração: {plano.duracao_meses} meses")
