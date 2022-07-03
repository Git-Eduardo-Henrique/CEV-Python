import math as mt
# =======================================================================
# calcula a hipotenusa
print(60 * "\033[32m=", "\033[m")
opo = float(input('Comprimento do \033[32mcateto oposto\033[m: '))
adi = float(input('Comprimento do \033[32mcateto adjacente\033[m: '))
hip = mt.hypot(opo, adi)
# =======================================================================
# mostra a hipotenusa
print(60 * "\033[32m=", "\033[m")
print(f'\033[32mhipotenusa\033[m do triangulo: \033[32m{hip:.2f}\033[m')
print(60 * "\033[32m=", "\033[m")
# =======================================================================
