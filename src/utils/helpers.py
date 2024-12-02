import re


def obter_numero_inteiro(
        mensagem, erro_mensagem="Erro: Digite um número válido.",
        min_valor=None, max_valor=None):
    while True:
        try:
            valor = int(input(mensagem))
            if ((min_valor is not None and valor < min_valor)
                or (max_valor is not None and valor > max_valor)):
                print(f"Erro: Insira um número entre {min_valor} e {max_valor}.")
            else:
                return valor
        except ValueError:
            print(erro_mensagem)


def validar_email(email):
    email_regex = r'^[a-zA-z0-9_.+-]+@[a-zA-Z0-9]+\.[a-zA-z0-9-.]+$'
    return re.match(email_regex, email) is not None


def validar_nome(nome):
    if nome.strip() and re.match(r"^[A-Za-zÀ-ÿ\s]+$", nome):
        return True
    return False