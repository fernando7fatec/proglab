


def validaCPF(cpf):
    contador = 10   
    soma = 0

    # Soma os 9 primeiros dígitos
    for i in range(11):
     if cpf[i] != '.':
       print(cpf[i], " i => ",contador, " = ", int(cpf[i]) * int(contador))
       soma = soma + int(cpf[i]) * int(contador) 
       contador = contador - 1
    print("\n",soma)

validaCPF('111.444.777-05')


# Lista de CPF Fake: 
# ---------------------
# 447.086.518-48
# 415.322.231-37
# 400.952.237-20
# ---------------------