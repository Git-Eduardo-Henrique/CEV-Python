def LeiaINT(Msg):
    """
    -> valida se é um numero ou não
    MSG = le a mensagem digitada para fazer a pergunta
    """
    while True:
        try:
            leia = int(input(Msg))
        except ValueError:
            print("\033[31mErro de tipo: Por favor digite um numero inteiro\033[m")
            print(34 * "\033[34m=", "\033[m")
        else:
            return leia


def LeiaFLOAT(Msg):
    while True:
        try:
            leia = float(input(Msg))
        except ValueError:
            print("\033[31mErro de tipo: Por favor digite um numero inteiro\033[m")
            print(34 * "\033[34m=", "\033[m")
        else:
            return leia


# ==================================================================================
# coleta de dados
print("\033[34m============[ EX 113 ]============")
print(34 * "=", "\033[m")
i = LeiaINT("Digite um \033[34mnumero inteiro\033[m: ")
f = LeiaFLOAT("Digite um \033[34mnumero real\033[m: ")
print(34 * "\033[34m=", "\033[m")
print(f"Inteiro: \033[34m{i}\033[m | Real: \033[34m{f}\033[m")
print(34 * "\033[34m=", "\033[m")
# ==================================================================================
