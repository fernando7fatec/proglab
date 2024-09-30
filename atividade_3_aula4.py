# ---------------------- #
#   ** BigData 4B  **    #
#    ╔═╗╔═╗╔╦╗╔═╗╔═╗     #
#    ╠╣ ╠═╣ ║ ║╣ ║       #
#    ╚  ╩ ╩ ╩ ╚═╝╚═╝     #
#    ** Ipiranga  **     #
#  << we take pride >>   #
# ---------------------- #

# ----------------------
# Aula 4  
# **********************
# Sep/19/24
# **********************
#
# Estrutura de loop
# Atividade 03 
# Fernando R. 
# ---------------------- 
# Classe EstruturaAula4
# implementando uma funçao para cada 
# exercicio e mais atividade bonus desafio 
# no final.
# ----------------------
class EstruturasAula4:

 # 1. Usando a estrutura de repetição while, crie um algoritmo que mostre os
 # primeiros 100 números pares.
 def imprimeCemNumerosPares():
    print(" --- Exercicio 1 --- ")
    for x in range(101):
     if x % 2 == 0:
      print(x)

 # 2. Altere o exercício 1 para que mostre os 100 primeiros números ímpares.
 def imprimeCemNumerosImpares():
    print(" --- Exercicio 2 --- ")
    for x in range(101):
     if x % 2 == 1:
      print(x)

# 3. Usando a estrutura de repetição while, crie um algoritmo que peça o usuário e a
# senha para um cadastro. O programa não pode permitir que o usuário seja igual a
# senha.
 def cadasTraUsuario():
    while True: 
        usuario = input(" Digite nome do usuario : ").strip()
        senha = input(" Digite uma nova senha : ").strip()
        if usuario != senha:
          print(" Usuario cadastrado com sucesso ! ")
          break
        else:
          print(" Usuario nao pode ser igual a senha ")

# 4. Usando a estrutura de repetição for, crie um algoritmo que separe os dígitos de
# um CPF qualquer.
 def cpfStriper(cpf):
    for a in cpf:
      if a != '.' and a != '-':
        print(a)

 # 5. Usando a estrutura de repetição for, crie um algoritmo que procure um
 # determinado nome em uma lista de nomes.
 def buscaNome(nome):
   nomes = ['Joao','Maria','Ana']
   for n in nomes:
     if nome == n:
       print("Nome consta na lista : ",n)

 ## Funcao Lambda para buscar nome em uma lista
 nomes = ['Joao','Maria','Ana']
 # retorna True se encontrar, False ao contrario.
 busca_nome = lambda nome,nomes : True if nome in nomes else False
 n = busca_nome('Joao',nomes)

 
 ## Funcao que ValidaCPF - Atividade Bonus - Desafio
 def validadorDeCPF(cpf):
    ''' Espera CPF como String '''
    # Se CPF for menor que 11 chars. retorna false
    if len(cpf) < 11:
        print(" CPF invalido ")
        return False    
    if cpf in [s * 11 for s in [str(n) for n in range(10)]]:
        print(" CPF invalido ")
        return False
    calcula = lambda t: int(t[1]) * (t[0] + 2)
    digito1 = (sum(map(calcula, enumerate(reversed(cpf[:-2])))) * 10) % 11
    digito2 = (sum(map(calcula, enumerate(reversed(cpf[:-1])))) * 10) % 11
    print(" CPF ",cpf, " Válido !!!! ")
    return str(digito1) == cpf[-2] and str(digito2) == cpf[-1]

# ---------------------
#  Lista de CPF mock: 
# ---------------------
#  447.086.518-48
#  415.322.231-37
#  400.952.237-20
# ---------------------

# Instancia classe EstruturaAula4
e = EstruturasAula4

# ---------------------
# Abaixo chamo 1 funcao 
# para cada exercicio
# ---------------------

# imprime 100 num pares
print("\n Exercicio 01 - 100 nums pares")
e.imprimeCemNumerosPares()

print("\n Exercicio 02 - 100 nums impares")
e.imprimeCemNumerosImpares()

print("\n Exercicio 03 - Cadastra Usuario ")
e.cadasTraUsuario()

print("\n Exercicio 04 - Imprime chars do CPF")
e.cpfStriper('41532223137')

# buscador de nome
print("\n Exercicio 05 - Busca nome :")
e.buscaNome('Maria')

print("\nBONUS -> Atividade Desafio - Validador de CPF")
# validador de cpf
e.validadorDeCPF('41532223137')
print("\n\n")