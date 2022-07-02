# ========================================================================
# calcula area de parede
print(45 * "\033[33m=", "\033[m")
larg = float(input('Largura da \033[33mparede\033[m (metros): '))
alt = float(input('Altura da \033[33mparede\033[m (metros): '))
area = larg * alt
# ========================================================================
# mostra area e tinta necessaria (2m² = 1L)
print(45 * "\033[33m=", "\033[m")
print(f'\033[33mArea\033[m da parede de \033[33m{larg} x {alt}\033[m: \033[33m{area}m²\033[m '
      f'\n\033[33mTinta\033[m necessária: \033[33m{area / 2}L\033[m')
print(45 * "\033[33m=", "\033[m")
# ========================================================================
