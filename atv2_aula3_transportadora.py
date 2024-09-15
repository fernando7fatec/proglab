# -------------------------
#  ** BigData Pride **
#    ╔═╗╔═╗╔╦╗╔═╗╔═╗
#    ╠╣ ╠═╣ ║ ║╣ ║  
#    ╚  ╩ ╩ ╩ ╚═╝╚═╝
#    ** Ipiranga  **
# -------------------------

# -------------------------
# Atividade 02 - Aula 03 
# Estruturas condicionais 
# -------------------------
class CalculadoraFrete:

 def calculaFrete(strTipoDeCaixa,intQtdeCaixa,fltDistancia):
    fltValorFrete = 0.0

    # Calcula o volume total 
    intVolumeTotal = (intQtdeCaixa * Caixa.tamanho(strTipoDeCaixa))

    # Escolhe o caminhao ideal, baseado no volume
    # caminhao = Caminhao.modeloIdeal(intVolumeTotal)
    caminhao = Caminhao.modeloIdeal(40)

    fltGastoGasolina = (caminhao[1])
    fltCustoGas = 5.48

    # Calcula o valor do frete já com o combustível
    fltValorFrete = round(((fltGastoGasolina * fltDistancia) * fltCustoGas),2)

    # Calcula a qtde de combustivel p/ o trajeto
    qtdeCombustivel = round((fltDistancia / caminhao[2]),2)
    
    print(" ---------------\n ")
    print(f"O Volume total a ser transportado será : {intVolumeTotal} m3")

    print(f"O {caminhao[0]} é o ideal para transportar essa carga")
    print(f"e irá consumir {qtdeCombustivel} lt de combustivel para o trajeto")
    print(f"com o valor do frete já com o combustivel : {fltValorFrete}")
    
    print("\n ---------------\n ")

class Caixa:
 def tamanho(tipo):
    # Volumes por tipo de caixas em m3
    fltA = 0.5
    fltB = 1.0
    fltC = 2.0 
    
    if tipo == "A":
        return fltA 
    elif tipo == "B":
        return fltB
    elif tipo == "C":
        return fltC
    else: 
        return None
  
class Caminhao:
    # modeloIdeal retorna array com modelo/capacidade/kmL
    def modeloIdeal(volume):
        if volume > 25 and volume <= 38:
           return ["Modelo 1",38,6]
        elif volume > 38  and volume <= 44:
           return ["Modelo 2",44,9]
        elif volume > 44 and volume <= 60:
           return ["Modelo 3",60,7]
        else:
           return [" Modelo indisponível para a carga "]

f = CalculadoraFrete

f.calculaFrete("C",20,100)


