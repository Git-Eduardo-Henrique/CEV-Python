from essentials import moeda

# ==================================================================================
# coleta de dados
print("\033[37m============[ EX 107 ]============")
print(34 * "=", "\033[m")
num = float(input("Digite um \033[37mvalor\033[m: "))
print(34 * "\033[37m=", "\033[m")
# ==================================================================================
# faz o dobro,metade e porcentagem
print(f"\033[37mDobro\033[m de {num}: \033[37m{moeda.dobro(num)}\033[m")
print(f"\033[37mMentade\033[m de {num}: \033[37m{moeda.metade(num)}\033[m")
print(f"\033[37mAumento em 10%\033[m de {num}: \033[37m{moeda.aumento(num, taxa=10)}\033[m")
print(f"\033[37mDiminuaçao em 10%\033[m de {num}: \033[37m{moeda.diminui(num, taxa=10)}\033[m")
print(34 * "\033[37m=", "\033[m")
# ==================================================================================
