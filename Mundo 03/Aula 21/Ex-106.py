def ajuda(com):
    help(com)


# ==================================================================================
# coleta de dados
print("\033[36m============[ EX 106 ]============\033[m")
while True:
    print(60 * "\033[36m=", "\033[m")
    h = str(input("digite uma \033[36mfunçao\033[m para ser \033[36manalisada\033[m [fim para parar]: "))
    if h == "fim":
        break
    else:
        print(60 * "\033[36m=", "\033[m")
        ajuda(h)
print(60 * "\033[36m=", "\033[m")
# ==================================================================================
