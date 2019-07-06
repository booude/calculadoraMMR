import random as rd
from statistics import mean
print("""Projeto em contrução por Booude.

CALCULADORA DE MMR
""")
elo = int(input("""Qual seu elo?
  1-Diamante  2-Platina  3-Ouro
  4-Prata     5-Bronze   6-Ferro
> """))
div = int(input("""Qual sua divisão?
> """))
vitorias = int(input("""Quantas vitórias você tem?
> """))
derrotas = int(input("""Quantas derrotas você tem?
> """))
pdl = int(input("""Quantos PdL você tem?
> """))
pdlv = int(input("""Quanto você ganha por vitória?
> """))
pdld = int(input("""Quanto você perde por derrota?
> """))
print("""
Aguarde...
""")
partidas = 0
decay = 0
falhou = 0
testes = 0
array=[]
winrate=[]
while testes < 100000:
  pdlr=pdl
  vitoriasr=vitorias
  derrotasr=derrotas
  while pdl < 100:
    winrate = vitorias/(vitorias+derrotas)*100
    toss = rd.randint(1,100)
    if toss <= winrate:
      vitorias += 1
      pdl = pdl + pdlv
      partidas+=1
      decay=0
    else:
      derrotas += 1
      pdl = pdl - pdld
      if pdl <= 0:
        pdl = 0
        decay+=1
      partidas+=1
    if decay > 4:
      falhou+=1
      decay=0
      partidas=0
  array.append(partidas)
  partidas=0
  testes+=1
  pdl=pdlr
  vitorias=vitoriasr
  derrotas=derrotasr
streak = array.count(min(array))
a = len(array)/100
while 0 in array:
  array.remove(0)
if div == 1:
  elo -=1
  if elo == 0:
    elo = "Mestre"
    div = -2
  elif elo == 1:
    elo = "Diamante"
  elif elo == 2:
    elo = "Platina"
  elif elo == 3:
    elo = "Ouro"
  elif elo == 4:
    elo = "Prata"
  elif elo == 5:
    elo = "Bronze"
  print("Em média, você chega na md5 para o",elo,div+3,"em",round(mean(array)),"partidas. ")
  print("Invicto, você chega na md5 para o",elo,div+3,"em",min(array),"partidas. ")
  print("Sua chance de ficar invicto por",min(array),"partidas é de "+str(streak/a)+"%. ")
  if elo == "Mestre":
    elo = "Diamante"
  elif elo == "Diamante":
    elo = "Platina"
  elif elo == "Platina":
    elo = "Ouro"
  elif elo == "Ouro":
    elo = "Prata"
  elif elo == "Prata":
    elo = "Bronze"
  elif elo == "Bronze":
    elo = "Ferro"
  print("Você tem "+str(falhou/a)+"% de chance de dropar para o",elo,"2. ")
else:
  if elo == 1:
    elo = "Diamante"
  elif elo == 2:
    elo = "Platina"
  elif elo == 3:
    elo = "Ouro"
  elif elo == 4:
    elo = "Prata"
  elif elo == 5:
    elo = "Bronze"
  elif elo == 6:
    elo = "Ferro"
  print("Em média, você chega na md3 para o",elo,div-1,"em",round(mean(array)),"partidas. ")
  print("Invicto, você chega na md3 para o",elo,div-1,"em",min(array), "partidas. ")
  print("Sua chance de ficar invicto por",min(array),"partidas é de "+str(streak/a)+"%. ")
  if div == 4:
    if elo == "Ferro":
      print("Tu é Ferro 4, seu lixo, fundo do poço. ")
    else:
        if elo == "Diamante":
            elo = "Platina"
        elif elo == "Platina":
            elo = "Ouro"
        elif elo == "Ouro":
            elo = "Prata"
        elif elo == "Prata":
            elo = "Bronze"
        elif elo == "Bronze":
            elo = "Ferro"
        print("Você tem "+str(falhou/a)+"% de chance de dropar para o",elo,"1. ")
  else:
    print("Você tem "+str(falhou/a)+"% de chance de dropar para o "+str(elo)+" "+str(div+1)+". ")