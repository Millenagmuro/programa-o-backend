#idade_completo.py

#carrega da biblioteca datetime a classe date
from datetime import date

#armazena na variável hoje o valor da função today da classe date
hoje = date.today()

#acessando o atributo ano dentro da função today
atual = int(hoje.strftime("%Y"))

nome = input("Qual o seu nome?\n")
ano = int(input("Qual ano você nasceu?\n"))
#Pergunta o  ano atual
#atual = int(input("Em qual ano estamos?\n")
idade = atual - ano
print("Olá, ", nome, "! Você tem", idade, "anos")

if idade >= 18:
        print("Você já pode dirigir!")
else:
    print("Você só pode andar de bicicleta!")
