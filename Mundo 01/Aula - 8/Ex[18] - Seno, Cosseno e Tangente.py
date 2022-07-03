import math as mt
# =======================================================================
# Coleta o angulo
print(60 * "\033[33m=", "\033[m")
ang = int(input('digite o \033[33mangulo\033[m: '))
print(60 * "\033[33m=", "\033[m")
# =======================================================================
# converte e mostra os resultados em (tangente, cosseno e seno)
print(f'Cos: \033[33m{mt.cos(mt.radians(ang)):.2f}\033[m'
      f'\nSeno: \033[33m{mt.sin(mt.radians(ang)):.2f}\033[m'
      f'\nTan: \033[33m{mt.tan(mt.radians(ang)):.2f}\033[m')
print(60 * "\033[33m=", "\033[m")
# =======================================================================
