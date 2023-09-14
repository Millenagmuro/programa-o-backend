#placar.py
#vencedor.py

primeiro_time = int(input("Digite o qual foi a quantidade de gols do primeiro time: "))
segundo_time = int(input("Digite o qual foi a quantidade de gols do segundo time: ")) 
if primeiro_time == segundo_time:
     print("Que pena, tivemos como resultado um empate.")
elif  primeiro_time > segundo_time:
     print("O primeiro time foi o vencedor, parabéns!!!!")
else:
     print("O segundo time foi o vencedor, parabéns!!!!")
