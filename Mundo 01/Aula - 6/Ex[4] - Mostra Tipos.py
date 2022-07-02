# tipo = coleta caracteres digitos para dizer seu tipo, se é numerio,etc..
# ========================================================================
# titulo e coleta de dados
print("\033[33m============[ EX 004 ]============")
print(34 * "=", "\033[m")
tipo = input("digite \033[33malgo\033[m: ")
print(34 * "\033[33m=", "\033[m")
# ========================================================================
# mostra informaçoes da variavel "tipo"
print(f"({tipo}) é do tipo: \033[33m{type(tipo)}\033[m")
print(f"({tipo}) é numero? \033[33m{tipo.isalnum()}\033[m")
print(f"({tipo}) é alpha numerico? \033[33m{tipo.isalpha()}\033[m")
print(f"({tipo}) é em minusculo? \033[33m{tipo.islower()}\033[m")
print(f"({tipo}) é em maiusculo? \033[33m{tipo.isupper()}\033[m")
print(f"({tipo}) so tem espaços? \033[33m{tipo.isspace()}\033[m")
# ========================================================================
