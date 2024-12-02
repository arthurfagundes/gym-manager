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