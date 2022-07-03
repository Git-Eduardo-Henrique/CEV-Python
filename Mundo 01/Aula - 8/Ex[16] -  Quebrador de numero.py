# =======================================================================
# pega o valor digitado
print(60 * "\033[31m=", "\033[m")
valor = float(input('digite um \033[31mnumero\033[m (decimal): '))
print(60 * "\033[31m=", "\033[m")
# =======================================================================
# converte e mostra o valor digitado
print(f'Valor \033[31mdigitado: {valor}\033[m\nValor \033[31mconvertido: {valor:.0f}\033[m'
      f'\nValor \033[31minteiro = {int(valor)}\033[m')
print(60 * "\033[31m=", "\033[m")
# =======================================================================
