homens_sexo = []
homens_idade = []
mulheres_sexo = []
mulheres_idade = []

for item in range(10):
    print('\n-- Pesquisa --')
    sexo = input('\nSexo(M | F): ')
    idade = int(input('Qual sua idade: '))
    if sexo in 'mM':
        homens_sexo.append(sexo)
        homens_idade.append(idade)
    else:
        mulheres_sexo.append(sexo)
        mulheres_idade.append(idade)

# A quantidade de homens e mulheres;
print("*")
print('\nResultado final da pesquisa\n')
print(f'\n\nQuantidade de Homens: {len(homens_sexo)}')
print(f'\nQuantidade de Mulheres: {len(mulheres_sexo)}')

# A média da idade dos homens e mulheres;
print(f'\nMédia de idade dos Homens: {sum(homens_idade) / len(homens_idade)}')
print(f'\nMédia de idade das Mulheres: {sum(mulheres_idade) / len(mulheres_idade)}')

# A maior idade entre os homens;
print(f'\nMaior idade entre os Homens: {max(homens_idade)}')

# *A maior idade entre as mulheres.
print(f'\nMaior idade entre as Mulheres: {max(mulheres_idade)}')
