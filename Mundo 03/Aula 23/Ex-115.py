from essentials import Interface

# ==================================================================================
# coleta de dados
arquivo = "Cev-Cadastro"
if not Interface.arquivo_ver(arquivo):
    Interface.criar_arq(arquivo)
print(Interface.menu(msg="\033[36mMenu Principal\033[m", tam=50))
