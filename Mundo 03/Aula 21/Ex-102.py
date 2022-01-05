def fac(num, show=False):
    """
    -> calcula o fatorial de um numero
    ==================================================
    num = numero para calcular factorial
    show = True: mostra o precesso, False: não mostra
    ==================================================
    return = resultado do factorial e o  processo
    ==================================================
    """
    resul = 1
    for cont in range(num, 0, -1):
        if show:
            if cont > 1:
                print(f"{cont} x", end=" ")
            else:
                print(f"{cont} =", end=" ")
        resul *= cont
    return f"\033[32m{resul}\033[m"


# ==================================================================================
# programa principal
# dec = decide se ira mostrar processor de calculo ou não
# dig = numero digitado para fatorial
dec = ""
# ==================================================================================
# coleta de dados
print("\033[32m============[ EX 102 ]============")
print(34 * "=", "\033[m")
dig = int(input("Digite um \033[32mnumero\033[m para ver seu \033[32mfactorial\033[m: "))
# ==================================================================================]
# ira pedir ate for igual a sim ou não
while True:
    dec = str(input("Deseja mostrar o \033[32mprocesso\033[m? [N/S] ")).upper()
    print(34 * "\033[32m=", "\033[m")
    # se for sim ira mostrar processo(true), senão não ira mostar  (false)
    if dec in "S":
        print(fac(dig, show=True))
        break
    elif dec in "N":
        print(fac(dig, show=False))
        break
# ==================================================================================
print(34 * "\033[32m=", "\033[m")
help(fac)
print(34 * "\033[32m=", "\033[m")
# ==================================================================================
