# Classe com funcoes/metodos
# quem convertem Celsius para F e vice-versa
# Aula - 2
# Professor Jobel 
# 5/9/24 - versão 0.1
# Aluno - Fernando Ramos

# Cria uma classe Conversor
class Conversor: 
    # Etapa 2 - Processa os dados
    # funcao que converte Celsius 
    # em F
    def converteCtoF(temperatura):
        F = float(9/5 * temperatura+ 32)
        return F
    
    # funcao que converte F em Celsius
    def converteFtoC(temperatura):
        C = float((temperatura-32)*5/9)
        return C

class EcoCar:
    def kmPorLitro(valor):
        litros = valor / 5
        km = litros * 20
        print(f"Você pode comprar {litros} de combustivel e rodar {km} km")

# -----------------
# Exercício 3 e 4 
# -----------------
cv = Conversor
print(" Digite 1 para converter Celsius para F ")
print(" Digite 2 para converter F para Celsius ")

# Usuario informa qual opcao de conversao
# Etapa 1 - Entrada de Dados
opcao = int(input(" Digite a opção : "))
temp = float(input(" Informe a temperatura a ser convertida : "))

# para opcao 1 chama funcao converteCtoF
# para opcao 2 chama funcao converteFtoF
# imprime o resultado na tela para ambas as funcoes.
if opcao == 1:
    # Etapa 3 - saída de dados
    print("CtoF : "+str(round(cv.converteCtoF(temp))))
else: 
    print("FtoC : "+str(round(cv.converteFtoC(temp))))