# ---------------------- #
#   ** BigData 4B  **    #
#    ╔═╗╔═╗╔╦╗╔═╗╔═╗     #
#    ╠╣ ╠═╣ ║ ║╣ ║       #
#    ╚  ╩ ╩ ╩ ╚═╝╚═╝     #
#    ** Ipiranga  **     #
#  << we take pride >>   #
# ---------------------- #

# -----------------------
# Atividade 04 - Aula 05 
# Listas em Python
# 26/09/24
# ------------------------

# ------------------------
# Classe VotaJogador
# Registra os votos do melhor
# jogador em campo feita por uma
# pesquisa.
# ------------------------
import sys

class VotaJogador:

 # Cria uma lista com 23 posições
 # com valor default 0. 
 votos = [0] * 23

 # Registra o voto em cada 
 # jogador.
 def registraVoto(camisa):
    if 0 <= camisa <= 23:
     VotaJogador.votos[camisa] += 1
     return True
    elif camisa == 0:
      print(" Programa encerrado ")
      sys.exit(0)
      return False
    else:
      raise Exception(" Jogador inexistente ")
      return True

 # imprime a Lista votos[]
 # com as respectiva camisas dos jogadores.
 def imprimeVotos():
    for j in range(len(VotaJogador.votos)):
      if j != 0 and VotaJogador.votos[j] != 0:
       print("camisa ", j,"  votos ->  ",VotaJogador.votos[j])
 
 # Faz um loop com o menu para que o usuário entre com a camisa
 # do jogador.
 def votacao():
  try:
   while True: 
       camisa = int(input(" Entre com a Camisa do Jogador: "))  # faz um prompt para o usuário entrar com a camisa.
       if 1 <= camisa <= 22:  # Considera camisas entre 1 e 22
         VotaJogador.registraVoto(camisa)
       elif camisa == 0:      # 0 encerra o programa
         print(" Votacao encerrada ")
         VotaJogador.imprimeVotos()
         sys.exit(1)
         return False
       elif camisa > 22:      # camisas maiores que 22, imprime uma msg.
         print(" Jogador Inexistente ")
  except ValueError:
    print( " . fim . ")

# Instancia uma classe VotaJogador.
v = VotaJogador
v.votacao()