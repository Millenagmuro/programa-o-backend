import pandas as pd
dados = pd.read_excel('tabela_paises.xlsx')
minha_coluna = []
for indice, linha in dados.iterrows():
    valor = linha['País']
    minha_coluna.append(valor)
print(minha_coluna)