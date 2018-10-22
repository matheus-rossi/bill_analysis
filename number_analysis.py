# import pandas
import pandas as pd

# Options to surpass scientific notation
pd.options.display.float_format = '{:.2f}'.format

# Path to data
file = 'data/data.xlsx'

# Load data
df = pd.read_excel(file)

# Drop UseLess Columns and change columns names
useful_df = df.drop(columns=['NOME', 'DEPARTAMENTO', 'CENTRO CUSTO'])
useful_df.rename(columns={'NÚMERO': 'NUMERO', 'NÚMERO DESTINO': 'NUMERO_DESTINO'}, inplace=True)

# Define number to Analise
number = input('Digite o número a ser Analisado: ')

# Categories classification
categories_not_useful = ['Descontos Linha', 'Parcelamento de Aparelhos', 'Assinatura Plano Voz', 'Gestao On Line',
                         'Tarifa Zero Nacional', 'Tarifa Zero Local', 'Outros']

categories_calls = ['Local Móvel', 'Local Fixo', 'Interurbano Móvel', 'Interurbano Fixo', 'Internacional']

categories_data = ['Consumo Dados']

# Custo da linha
number_cost = useful_df.query('NUMERO == @number')
if number_cost.empty:
    number_cost = 'Número Não Encontrado'
else:
    number_cost = number_cost['VALOR'].sum().round(2)

filtered_df = useful_df.query('NUMERO == @number and CATEGORIA not in @categories_not_useful ')

# Filter DF by number
filtered_df = useful_df.query('NUMERO == @number and CATEGORIA not in @categories_not_useful ')

# Sum call categories
number_calls = filtered_df.query('NUMERO == @number and CATEGORIA in @categories_calls ')
number_calls = number_calls['MINUTOS'].sum()

# Sum data categories
number_data = filtered_df.query('NUMERO == @number and CATEGORIA in @categories_data ')
number_data = number_data['MEGA'].str.replace(',', '.').astype(float).sum().round(2)

# Check if DataFrame is empty
if filtered_df.empty:
    print('Este número não registrou ligações e consumo de dados no período analisado')
else:
    print('Minutos Consumidos: ', number_calls)
    print('Dados Consumidos: ', number_data)

print('Custo da Linha: ', number_cost)
