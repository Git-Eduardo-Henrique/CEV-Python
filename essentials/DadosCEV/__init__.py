def LeiaDinheiro(msg):
    valido = False
    while not valido:
        mens = str(input(msg)).replace(',', '.')
        if mens.isalpha() or mens.strip() == '':
            print("\033[31mERRO! tente algo valido\033[m")
        else:
            valido = True
            return float(mens)