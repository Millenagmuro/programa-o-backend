import pandas as pd
import json

dados = pd.read_excel('tabela_paises.xlsx')
dados.set_index('Posição', inplace=True)
num_teste = input("Qual dado deseja salvar?")
teste = 'País'
dicionario = {}

for indice, linha in dados.iterrows():
    chave = indice
    valor = linha[teste]
    dicionario[chave] = valor

print(dicionario)

dados_json = json.dumps(dicionario)

print(dados_json)