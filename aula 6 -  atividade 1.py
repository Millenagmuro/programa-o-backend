#importa as bibliotecas
#instalar com "py - pip install pandas" "py -m pip install openpyxl"

import pandas as pd

dados = pd.read_excel('perfis_lp.xlsx')

print(dados)

indice = int(input("Qual teste deseja mostrar? Digite o número da linha:"))

print(dados.loc[[indice]])

nome = input("Qual nome deseja mostrar?")
nomes = dados.set_index('Nome')

print(nomes.loc[nome])

num_teste = input("Qual teste deseja imprimir?")

teste = 'teste' +num_teste
print("Opção Selecionada:", teste)

print(nomes.loc[nome, teste])
