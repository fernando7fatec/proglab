def validadorDeCPF(cpf):
    ''' Espera CPF como String '''
    # Se CPF for menor que 11 chars. retorna false
    if len(cpf) < 11:
        return False    
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        return False
    calcula = lambda t: int(t[1]) * (t[0] + 2)
    digito1 = (sum(map(calcula, enumerate(reversed(cpf[:-2])))) * 10) % 11
    digito2 = (sum(map(calcula, enumerate(reversed(cpf[:-1])))) * 10) % 11

    return str(digito1) == cpf[-2] and str(digito2) == cpf[-1]

cpf2 = validadorDeCPF('44646759993')

if cpf2 == True:
    print(" CPF válido ")
else:
    print(" CPF inválido ! ")