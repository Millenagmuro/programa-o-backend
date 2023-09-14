#maior_ou_menor.py

numero1 = int(input("Digite o primeiro número de sua escolha: "))
numero2 = int(input("Digite o segundo número de sua escolha: "))

if numero1<numero2:
    maior=numero2
    menor=numero1

else:
    maior=numero1
    menor=numero2


print(f"o maior número é: {maior}")
print(f"o menor número é: {menor}")
