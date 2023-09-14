#classificação.py

idade = int(input("Qual é a idade que o nadador possuí: "))

if idade >= 5 and idade <= 7:
    categoria = "Infantil A"
elif idade <= 11:
    categoria = "Infantil B"
elif idade <= 13:
    categoria = "Juvenil A"
elif idade <= 17:
    categoria = "Juvenil B"
else:
    categoria = "Adultos"

 

print("A categoria em que o nadador está é:", categoria)
