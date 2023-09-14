import pandas as pd
import matplotlib.pyplot as plt

url = "https://github.com/Millenagmuro/raw/tabela_pais.xlsx"
dados = pd.read_excel(url)

print(dados)

num_coluna = input("Qual teste deseja contar as repetições?")
coluna = 'coluna' + num_coluna
contagem = dados[num_coluna].value_counts()
print(contagem)

contagem.plot.bar(color=['blue','red','green'], ec = 'k', alpha = 0.5)
plt.xticks(notation=360, fontsize=12)
plt.xticks(fontsize=12)
plt.show()