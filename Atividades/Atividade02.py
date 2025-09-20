# Escreva uma função que receba uma lista de números e retorne outra lista com os números ímpares.

def numeros_impares(lista):
    return [num for num in lista if num % 2 != 0]

# 2. Escreva uma função que receba uma lista de números e retorne outra lista com os números primos presentes.

def numeros_primos(lista):
    return [
        n for n in lista
        if n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
    ]

# 3. Escreva uma função que receba duas listas e retorne outra lista com os elementos que estão presentes em apenas uma das listas.

def elementos_exclusivos(lista1, lista2):
    return list(set(lista1) ^ set(lista2))  # XOR entre os conjuntos

# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o segundo maior valor na lista.

def segundo_maior(lista):
    if len(lista) < 2:
        return None
    lista_elementos_unicos = list(set(lista))
    lista_elementos_unicos.sort(reverse=True)
    return lista_elementos_unicos[1] if len(lista_elementos_unicos) >= 2 else None
    
# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das pessoas em ordem alfabética.

def ordenar_por_nome(lista_tuplas):
    return sorted(lista_tuplas, key=lambda tupla: tupla[0])

# 6. Como identificar e tratar outliers em uma coluna numérica usando desvio padrão ou quartis?

def remover_outliers_desvio(df, coluna):
    media = df[coluna].mean()
    desvio = df[coluna].std()
    return df[(df[coluna] > media - 3*desvio) & (df[coluna] < media + 3*desvio)]

def remover_outliers_iqr(df, coluna):
    Q1 = df[coluna].quantile(0.25)
    Q3 = df[coluna].quantile(0.75)
    IQR = Q3 - Q1
    return df[(df[coluna] >= Q1 - 1.5 * IQR) & (df[coluna] <= Q3 + 1.5 * IQR)]

# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), mesmo que tenham colunas diferentes? Dica: Utiliza-se pd.concat() especificando axis=0 (linhas) ou axis=1 (colunas). Quando há colunas diferentes, os valores ausentes são preenchidos com NaN.

df_concatenado_linhas = pd.concat([df1, df2], axis=0)
df_concatenado_colunas = pd.concat([df1, df2], axis=1)

# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

df = pd.read_csv('arquivo.csv')
print(df.head())

# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

coluna_valor = df['valor']
df_filtrado = df[df['valor'] == 42]    # Filtra linhas onde 'valor' é igual a 42.

# 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

df.isnull()    # Verifica valores ausentes

df_sem_nan = df.dropna()    # Remove linhas com NaN

df_preenchido = df.fillna(0)    # Preenche NaNs com um valor específico

df['coluna'] = df['coluna'].fillna(df['coluna'].mean())    # Preenche com a média da coluna
