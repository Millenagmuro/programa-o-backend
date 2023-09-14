import pandas as pd
import json
# Altere a linha abixo para o nome do seu arquivo Excel
dados = pd.read_excel('tabela_paises.xlsx')
#Altere a linha abaixo para a coluna que deseja utilizar como indice
dados.set_index('Posição', inplace=True)
num = 0
print("Escolha uma opção:")
for nome_colunas in dados.columns:
    num += 1
    print(f'Digite {num} para mostrar a coluna', nome_colunas)
opcao = int(input("Digite o número da opção desejada: "))
conj_colunas = list(dados.columns)
if opcao == 1:
    coluna = conj_colunas[0]
elif opcao == 2:
    coluna = conj_colunas[1]
elif opcao == 3:
    coluna = conj_colunas[2]
elif opcao == 4:
    coluna = conj_colunas[3]
else:
    print("Opção inválida.")

dicionario = {}
for indice, linha in dados.iterrows():
    chave = indice
    valor = linha[coluna]
    dicionario[chave] = valor
for chave, valor in dicionario.items():
    print(f'{chave}, {valor}')

dados_json = json.dumps(dicionario)
print(dados_json)