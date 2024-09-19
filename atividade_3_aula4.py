# -----------------------------------
# Aula 4 - Estrutura de loop
# Atividade 03 
# -----------------------------------
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

e = EstruturasAula4
e.buscaNome('Maria')

# ---------------------
#  Lista de CPF Fake: 
# ---------------------
#  447.086.518-48
#  415.322.231-37
#  400.952.237-20
# ---------------------