from random import choice
# =======================================================================
# coleta informações dos alunos
print(60 * "\033[34m=", "\033[m")
aluno1 = str(input('Digite o nome do \033[34maluno 1\033[m: '))
aluno2 = str(input('Digite o nome do \033[34maluno 2\033[m: '))
aluno3 = str(input('Digite o nome do \033[34maluno 3\033[m: '))
aluno4 = str(input('Digite o nome do \033[34maluno 4\033[m: '))
# =======================================================================
# escolhe e mostra o aluno escolhido
print(60 * "\033[34m=", "\033[m")
lista = [aluno1, aluno2, aluno3, aluno4]
print(f'O aluno \033[34mescolido\033[m foi: \033[34m{choice(lista)}\033[m')
print(60 * "\033[34m=", "\033[m")
# =======================================================================
