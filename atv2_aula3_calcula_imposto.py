# ---------------------- #
#   ** BigData 4B  **    #
#    ╔═╗╔═╗╔╦╗╔═╗╔═╗     #
#    ╠╣ ╠═╣ ║ ║╣ ║       #
#    ╚  ╩ ╩ ╩ ╚═╝╚═╝     #
#    ** Ipiranga  **     #
#  << we take pride >>   #
# ---------------------- #

# -----------------------
# Atividade 02 - Aula 03 
# Estruturas condicionais 
# 12/09/24
# ------------------------

# Implementa classe 
# e seus métodos
# para o calculo de imposto sobre salário.

class CalculaImposto:
    def calculaImposto(salario):

        # Input dados
        fltSalario = float(salario)
         
        # processo os dados
        fltIR = CalculaImposto.calculaIR(salario)
        fltINSS = CalculaImposto.calculaINSS(salario)

        salario_liq = CalculaImposto.formatarReais(salario - (fltIR + fltINSS))

        # saída dos dados
        print(f"Salario liquido : {salario_liq}")
        
    # Funcao que calcula imposto de renda
    def calculaIR(salario):
        fltImpostoRenda = 0

        # Processa os dados
        if salario < 2112.00:
            fltImpostoRenda = 0 
        elif salario > 2112.00 and salario < 2826.85:
            fltImpostoRenda = (salario * 0.075)
        elif salario > 2826.85 and salario < 3751.05:
            fltImpostoRenda = (salario * 0.15)
        elif salario > 3751.05 and salario < 4664.68:
            fltImpostoRenda = (salario * 0.2265)
        elif salario > 4664.68:
            fltImpostoRenda = (salario * 0.275)

        return fltImpostoRenda

    # Calcula e retorna o valor do INSS
    # Baseado na tabela fornecida
    def calculaINSS(salario):
        fltINSS = 0

        # Processa os dados
        if salario < 1302.00:
            fltINSS = (salario * 0.075) 
        elif salario > 1302.01 and salario < 2571.29:
            fltINSS = (salario * 0.090)
        elif salario > 2571.29 and salario < 3856.94:
            fltINSS = (salario * 0.12)
        elif salario >  3856.94 and salario < 7507.49:
            fltINSS = (salario * 0.14)
        return fltINSS 

    # Funcao helper
    # que formata um valor para Reais(Brasil) (R$)
    # com duas casas decimais.
    def formatarReais(valor):
        formato = "R$ {:,.2f}".format(valor)
        return formato


calC = CalculaImposto

print(" -----  \n")
calC.calculaImposto(2000)
print(" \n-----  \n")
