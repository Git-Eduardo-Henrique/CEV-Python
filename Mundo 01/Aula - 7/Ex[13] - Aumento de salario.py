# =======================================================================
# calcula aumento do salario do funcionario
print(60 * "\033[35m=", "\033[m")
salario = float(input('\033[35mSalario\033[m do funcionário: \033[35mR$\033[m'))
aume = salario + (salario * 15 / 100)
# =======================================================================
# mostra o salario com aumento
print(60 * "\033[35m=", "\033[m")
print(f'Salario de \033[35mR${salario:.2f}\033[m com aumento '
      f'de \033[35m15%\033[m: \033[35mR${aume:.2f}\033[m')
print(60 * "\033[35m=", "\033[m")
# =======================================================================
