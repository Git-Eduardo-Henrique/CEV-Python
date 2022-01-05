from time import sleep


def arquivo_ver(name):
    try:
        file = open(name, 'rt')
        file.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arq(name):
    try:
        file = open(name, "wt+")
        file.close()
    except:
        print("ERRO 404")
    else:
        print("Arquivo foi criado com sucesso :)")


def Ler_arq(name='Cev-Cadastro'):
    try:
        file = open(name, 'rt')
    except:
        print("ERRO 909")
    else:
        for pessoa in file:
            dados = pessoa.split(',')
            print(f"nome: \033[34m{dados[0]}\033[m idade: \033[34m{dados[1]}\033[m")


def Gravar_arq(name='Cev-Cadastro'):
    try:
        file = open(name, 'at')
    except:
        print('erro 606')
    else:
        pessoas = dict()
        nome = str(input('\033[35mNome\033[m: '))
        idade = str(input('\033[35mIdade\033[m: '))
        pessoas["nome"] = nome
        pessoas["idade"] = idade
        file.write('\n')
        file.write(pessoas["nome"])
        file.write(',')
        file.write(pessoas["idade"])
        file.close()


def menu(msg="menu", tam=42):
    pessoas = dict()
    while True:
        # ===================================================================
        # cria o cabeçalho
        print("=" * tam)
        print(f"{msg.center(tam)}")
        print('=' * tam)
        print("\033[31m1\033[m - \033[34mVer pessoas cadastradas\033[m")
        print("\033[31m2\033[m - \033[34mCadastrar uma nova pessoa\033[m")
        print("\033[31m3\033[m - \033[34mSair do sistema\033[m")
        print("=" * tam)
        # ===================================================================
        # verifica as opçoes
        while True:
            try:
                opt = int(input("Selecione uma \033[34mopçao\033[m: "))
            except ValueError:
                print("\033[31mErro,por favor digite um numero\033[m")
            else:
                if opt > 3 or opt < 0:
                    print("\033[31mErro, digite uma opçao valida\033[m")
                    break
                else:
                    break
        # ===================================================================
        # define cada opçao
        if opt == 1:
            print("=" * tam)
            print(f"{'Pessoas Cadastradas: '.center(tam)}")
            print("=" * tam)
            Ler_arq()
            print("=" * tam)
            break
        elif opt == 2:
            print("=" * tam)
            print(f"{'Cadastrar Pessoas: '.center(tam)}")
            print("=" * tam)
            # =========================================
            Gravar_arq()
            print("=" * tam)
            # ==========================================
            break
        elif opt == 3:
            print("=" * tam)
            break
    # ===================================================================
    # encerra o programa
    print("\033[36mencerrando programa\033[m", end='')
    for cont in range(0, 3):
        sleep(0.4)
        if cont < 2:
            print(".", end='')
        else:
            print(".")
    return '=' * tam
    # ===================================================================
