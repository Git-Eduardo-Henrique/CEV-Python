from random import shuffle
# =======================================================================
# coleta e organisa a lista de alunos
print(60 * "\033[35m=", "\033[m")
aluno1 = str(input('Digite o nome do \033[35maluno 1\033[m: '))
aluno2 = str(input('Digite o nome do \033[35maluno 2\033[m: '))
aluno3 = str(input('Digite o nome do \033[35maluno 3\033[m: '))
aluno4 = str(input('Digite o nome do \033[35maluno 4\033[m: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
# =======================================================================
# mostra a nova lista
print(60 * "\033[35m=", "\033[m")
print(f'a \033[35mordem\033[m ficou: \033[35m{lista}\033[m')
print(60 * "\033[35m=", "\033[m")
# =======================================================================
