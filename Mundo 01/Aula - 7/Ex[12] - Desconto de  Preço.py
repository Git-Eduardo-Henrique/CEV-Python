# =======================================================================
# calcula desconto do produto
print(60 * "\033[34m=", "\033[m")
Preco = float(input('\033[34mPreço\033[m do Produto: \033[34mR$\033[m'))
Desc = Preco - (Preco * 5 / 100)
# =======================================================================
# mostra o valor do produto com desconto
print(60 * "\033[34m=", "\033[m")
print(f'O produto que custa R$\033[34m{Preco:.2f}\033[m com desconto de '
      f'\033[34m5%\033[m: R$\033[34m{Desc:.2f}\033[m')
print(60 * "\033[34m=", "\033[m")
# =======================================================================
