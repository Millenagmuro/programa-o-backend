num = int(input(f"digite um numero 1: "))
maior_numero = num
menor_numero = num
soma = 0
i = 1
for i in range(10):
    num = int(input(f"digite um numero {i+1}: "))
    soma = soma + num
    if num > maior_numero:
        maior_numero = num
    if num < menor_numero:
        menor_numero = num

print("a media é: ", soma / 10)
print(f"o maior numero foi: {maior_numero}")
print(f"o menor numero foi: {menor_numero}")
