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


# Categories classification
categories_not_useful = ['Descontos Linha', 'Parcelamento de Aparelhos', 'Assinatura Plano Voz', 'Gestao On Line',
                         'Tarifa Zero Nacional', 'Tarifa Zero Local', 'Outros']

categories_calls = ['Local Móvel', 'Local Fixo', 'Interurbano Móvel', 'Interurbano Fixo']

categories_tariffs = ['Tarifa Zero Nacional', 'Tarifa Zero Local']

categories_data = ['Consumo Dados']

# Minutes Consumed
min_consume = useful_df['MINUTOS'].sum().round(2)

# Cost of local_mobile
local_mobile = useful_df.query('CATEGORIA == "Local Móvel"')
local_mobile = local_mobile['MINUTOS'].sum().round(2)

# Cost of local_fixed
local_fixed = useful_df.query('CATEGORIA == "Local Fixo"')
local_fixed = local_fixed['MINUTOS'].sum().round(2)

# Cost of intercity mobile
intercity_mobile = useful_df.query('CATEGORIA == "Interurbano Móvel"')
intercity_mobile = intercity_mobile['MINUTOS'].sum().round(2)

# Cost of intercity fixed
intercity_fixed = useful_df.query('CATEGORIA == "Interurbano Fixo"')
intercity_fixed = intercity_fixed['MINUTOS'].sum().round(2)

# Cost of international_calls
international_calls = useful_df.query('CATEGORIA == "Internacional"')
international_calls = international_calls['MINUTOS'].sum().round(2)

print('\nConsumo Total: ', min_consume)
print('Consumo Total Local Móvel: ', local_mobile)
print('Consumo Total Local Fixo: ', local_fixed)
print('Consumo Total Interurbano Móvel: ', intercity_mobile)
print('Consumo Total Interurbano Fixo: ', intercity_fixed)
print('Consumo Total Internacional: ', international_calls)


