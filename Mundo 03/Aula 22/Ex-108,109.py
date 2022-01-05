from essentials import MoedaUpdate

# ==================================================================================
# coleta de dados
print("\033[31m============[ EX 108-109 ]============")
print(38 * "=", "\033[m")
num = float(input("Digite um \033[31mvalor\033[m: \033[31mR$\033[m"))
print(38 * "\033[31m=", "\033[m")
# ==================================================================================
# faz o dobro,metade e porcentagem
print(f"\033[31mDobro\033[m de {MoedaUpdate.tipo(num)}: \033[31m{(MoedaUpdate.dobro(num, formato=True))}\033[m")
print(f"\033[31mMentade\033[m de {MoedaUpdate.tipo(num)}: \033[31m{MoedaUpdate.metade(num, formato=True)}\033[m")
print(f"\033[31mAumento em 10%\033[m de {MoedaUpdate.tipo(num)}: "
      f"\033[31m{MoedaUpdate.aumento(num, taxa=10, formato=True)}\033[m")
print(f"\033[31mDiminuaçao em 10%\033[m de {MoedaUpdate.tipo(num)}: "
      f"\033[31m{MoedaUpdate.diminui(num, taxa=10, formato=True)}\033[m")
print(38 * "\033[31m=", "\033[m")
# ==================================================================================
