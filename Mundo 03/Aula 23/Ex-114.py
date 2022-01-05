import urllib.request

# ==================================================================================
# coleta de dados
print("\033[35m============[ EX 114 ]============")
print(34 * "=", "\033[m")
try:
    pudim = urllib.request.urlopen("http://pudim.com.br")
except urllib.request.URLError:
    print("O site: \033[35mpudin.com.br\033[m não esta acessivel no momento :(")
else:
    print("Consegui acessar o site: \033[35mpudin.com.br\033[m com sucesso :D")
print(34 * "\033[35m=", "\033[m")
