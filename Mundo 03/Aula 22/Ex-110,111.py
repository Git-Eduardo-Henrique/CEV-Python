from essentials import MoedaUpdate

# ==================================================================================
# coleta de dados
print("\033[32m============[ EX 110-111 ]============")
print(34 * "=", "\033[m")
num = float(input("Digite um \033[32mvalor\033[m: \033[32mR$\033[m"))
print(34 * "\033[32m=", "\033[m")
# ==================================================================================
# faz o dobro,metade e porcentagem
MoedaUpdate.resumo(num, 10, 10, formato=True)
print(34 * "\033[32m=", "\033[m")
# ==================================================================================
