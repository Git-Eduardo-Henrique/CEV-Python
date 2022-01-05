from essentials import MoedaUpdate
from essentials import DadosCEV
# ==================================================================================
# coleta de dados
print("\033[33m============[ EX 112]============")
print(34 * "=", "\033[m")
num = DadosCEV.LeiaDinheiro("Digite um \033[33mvalor\033[m: \033[33mR$\033[m")
print(34 * "\033[33m=", "\033[m")
# ==================================================================================
# faz o dobro,metade e porcentagem
MoedaUpdate.resumo(num, 10, 10, formato=True)
print(34 * "\033[33m=", "\033[m")
# ==================================================================================
