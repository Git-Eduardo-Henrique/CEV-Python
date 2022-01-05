def voto(vote):
    """
    =================================================================
    :year: = coleta o data do pc
    =================================================================
    :idade: = calcula a idade com base na data do pc e comando(vote)
         Ex: voto(2000)
             idade  = year - 2000
    =================================================================
    se idade for menor que 16 :return: Negado
    se idade for maior que 16 e menor que 18 :return: Opcional
    se idade for maior que 18 :return: Obrigatorio
    =================================================================
    """
    from datetime import date
    year = date.today().year
    idade = year - vote
    if idade < 16:
        return f"Com \033[31m{idade}\033[m anos: \033[31mVoto Negado\033[m!"
    elif 16 <= idade < 18:
        return f"Com \033[31m{idade}\033[m anos: \033[31mVoto Opcional\033[m!"
    else:
        return f"Com \033[31m{idade}\033[m anos: \033[31mVoto Obrigatorio\033[m!"


# ==================================================================================
# programa principal
# nasc = data de nascimento
print("\033[31m============[ EX 101 ]============")
print(34 * "=", "\033[m")
nasc = int(input("Digite seu \033[31mano\033[m de nascimento: "))
print(34 * "\033[31m=", "\033[m")
print(voto(nasc))
print(34 * "\033[31m=", "\033[m")
help(voto)
# ==================================================================================
