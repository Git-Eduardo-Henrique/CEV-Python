def ficha(name="[Desaconhecido]", goal=0):
    """
    ==========================================================
    -> escreve quantos gols tal jogador realizou na temporada
    ==========================================================
    name = recebe o nome do jogador
    goal = recebe gols do jogador
    ==========================================================
    return: nome e gols do jogador
    """
    return f"O jogador \033[33m{name}\033[m realizou \033[33m{goal}\033[m gols no campeonato"


# ==================================================================================
# nome = nome do jogador
# gols = gols realizados pelo jogador
# coleta de dados
print("\033[33m============[ EX 103 ]============")
print(34 * "=", "\033[m")
nome = str(input("Nome do \033[33mJogador\033[m: "))
gols = str(input("Gols do \033[33mjogador\033[m: "))
# ===================================================================================
# se gols for um numero ira deixar de ser str
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
# se nome for nulo ira mostrar apenas gols
if nome.strip() == '':
    print(34 * "\033[33m=", "\033[m")
    print(ficha(goal=gols))
    print(34 * "\033[33m=", "\033[m")
else:
    print(34 * "\033[33m=", "\033[m")
    print(ficha(nome, gols))
    print(34 * "\033[33m=", "\033[m")
help(ficha)
# ===================================================================================
