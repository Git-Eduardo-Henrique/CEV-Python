def LeiaINT(Msg):
    """
    -> valida se é um numero ou não
    MSG = le a mensagem digitada para fazer a pergunta
    """
    valor = 0
    while True:
        leia = str(input(Msg))
        if leia.isnumeric():
            valor = int(leia)
            print(34 * "\033[34m=", "\033[m")
            print(f"voce digitou o numero: \033[34m{valor}\033[m")
            print(34 * "\033[34m=", "\033[m")
            break
        else:
            print("\033[34mErro! Digite um numero\033[m")


# ==================================================================================
# coleta de dados
print("\033[34m============[ EX 104 ]============")
print(34 * "=", "\033[m")
LeiaINT("Digite um \033[34mnumero\033[m: ")
# ==================================================================================
