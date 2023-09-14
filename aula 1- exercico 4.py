#idade.py

nome = input("Qual o seu nome?\n")
ano_nasc = int(input("Qual ano você nasceu?\n") )
ano_atual = int(input("Em qual ano estamos?\n") )
idade = ano_atual - ano_nasc
print("Olá", nome, "! Você tem", idade, "anos")
