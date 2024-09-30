NOVO_CPF = list(input("Digite um CPF para ser validado >>>"))
NOVO_CPF_STRING = " ".join(NOVO_CPF)

def validacao_cpf():
  if len(NOVO_CPF) == 11:
      primeiro1 = int(NOVO_CPF[0]) * 10
      primeiro2 = int(NOVO_CPF[1]) * 9
      primeiro3 = int(NOVO_CPF[2]) * 8
      primeiro4 = int(NOVO_CPF[3]) * 7
      primeiro5 = int(NOVO_CPF[4]) * 6
      primeiro6 = int(NOVO_CPF[5]) * 5
      primeiro7 = int(NOVO_CPF[6]) * 4
      primeiro8 = int(NOVO_CPF[7]) * 3
      primeiro9 = int(NOVO_CPF[8]) * 2

      seg_primeiro1 = int(NOVO_CPF[0]) * 11
      seg_primeiro2 = int(NOVO_CPF[1]) * 10
      seg_primeiro3 = int(NOVO_CPF[2]) * 9
      seg_primeiro4 = int(NOVO_CPF[3]) * 8
      seg_primeiro5 = int(NOVO_CPF[4]) * 7
      seg_primeiro6 = int(NOVO_CPF[5]) * 6
      seg_primeiro7 = int(NOVO_CPF[6]) * 5
      seg_primeiro8 = int(NOVO_CPF[7]) * 4
      seg_primeiro9 = int(NOVO_CPF[8]) * 3
      seg_primeiro10 = int(NOVO_CPF[9]) * 2

      soma_validacao = (primeiro1 + primeiro2 + primeiro3 + primeiro4 + primeiro5 + primeiro6 + primeiro7 + primeiro8 + primeiro9)
      divisao_soma = (soma_validacao // 11)
      resto = (soma_validacao - (11 * divisao_soma))

      soma_validacao_2 = (seg_primeiro1 + seg_primeiro2 + seg_primeiro3 + seg_primeiro4 + seg_primeiro5 + seg_primeiro6 + seg_primeiro7 + seg_primeiro8 + seg_primeiro9 + seg_primeiro10)
      divisao_soma_2 = (soma_validacao_2 // 11)
      resto_2 = (soma_validacao_2 - (11 * divisao_soma_2))

      val_1 = False
      val_2 = False
      val_3 = False
      val_4 = False

      if(resto <=1) and (NOVO_CPF[9] == 0):
          val_1 = True
      if( resto >=2 and resto < 10) and (11 - resto == NOVO_CPF[9]):
          val_2 = True
      if( resto_2 <=1 ) and (NOVO_CPF[10] == 0):
          val_3 = True
      if ( resto_2 >=2 and resto_2 < 10 ) and (11 - resto_2 == NOVO_CPF[10]):
          val_4 = True
      else: ()

      if (val_1 == True or val_2 == True) and (val_3 == True or val_4 == True):
          print(f"O CPF número: {NOVO_CPF_STRING} é válido !")
      else:
          print(f"O CPF número: {NOVO_CPF_STRING} é inválido, tente novamente.")
  else: 
      print(f"O CPF número: {NOVO_CPF_STRING} é inválido, tente novamente.")

validacao_cpf()