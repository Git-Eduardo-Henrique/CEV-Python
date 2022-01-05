def notas(*dic, sit=False):
    r = dict()
    r['total'] = len(dic)
    r['maior'] = max(dic)
    r['menor'] = min(dic)
    r['media'] = sum(dic)/ len(dic)
    if sit:
        if r['media'] >= 7:
            r['sit'] = "\033[35mBOA\033[m]"
        elif r['media'] >= 5:
            r['sit'] = "\033[35mRAZOAVEL\033[m"
        else:
            r['sit'] = "\003[35mRUIM\033[m"
    return r


# ==================================================================================
# coleta de dados
print("\033[35m============[ EX 105 ]============")
print(34 * "=", "\033[m")
resp = notas(5, 6, 7, 9, sit=True)
print(resp)
print(34 * "\033[35m=", "\033[m")
# ==================================================================================
