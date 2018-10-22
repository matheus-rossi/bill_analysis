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

# Define available analysis
print('Análises disponíveis: \n 01 -> Visão Geral (R$) \n 02 -> Ligações (R$)  \n 03 -> Consumo Dados (R$) \n')
analysis_number = input('Digite o número da análise desejada: ')

# Categories classification
categories_not_useful = ['Descontos Linha', 'Parcelamento de Aparelhos', 'Assinatura Plano Voz', 'Gestao On Line',
                         'Tarifa Zero Nacional', 'Tarifa Zero Local', 'Outros']

categories_calls = ['Local Móvel', 'Local Fixo', 'Interurbano Móvel', 'Interurbano Fixo']

categories_tariffs = ['Tarifa Zero Nacional', 'Tarifa Zero Local']

categories_data = ['Consumo Dados']

# Cost of bill
bill_cost = useful_df['VALOR'].sum().round(2)

# Cost of discounts
discount = useful_df.query('CATEGORIA == "Descontos Linha"')
discount = discount['VALOR'].sum().round(2)

# Cost of phones installments
phones_installments = useful_df.query('CATEGORIA == "Parcelamento de Aparelhos"')
phones_installments = phones_installments['VALOR'].sum().round(2)

# Cost of voice plan
voice_plan = useful_df.query('CATEGORIA == "Assinatura Plano Voz"')
voice_plan = voice_plan['VALOR'].sum().round(2)

# Cost of online management
online_management = useful_df.query('CATEGORIA == "Gestao On Line"')
online_management = online_management['VALOR'].sum().round(2)

# Cost of tariffs
tariffs = useful_df.query('CATEGORIA in @categories_tariffs')
tariffs = tariffs['VALOR'].sum().round(2)

# Cost of others
others = useful_df.query('CATEGORIA == "Outros"')
others = others['VALOR'].sum().round(2)

# Cost of local_mobile
local_mobile = useful_df.query('CATEGORIA == "Local Móvel"')
local_mobile = local_mobile['VALOR'].sum().round(2)

# Cost of local_fixed
local_fixed = useful_df.query('CATEGORIA == "Local Fixo"')
local_fixed = local_fixed['VALOR'].sum().round(2)

# Cost of intercity mobile
intercity_mobile = useful_df.query('CATEGORIA == "Interurbano Móvel"')
intercity_mobile = intercity_mobile['VALOR'].sum().round(2)

# Cost of intercity fixed
intercity_fixed = useful_df.query('CATEGORIA == "Interurbano Fixo"')
intercity_fixed = intercity_fixed['VALOR'].sum().round(2)

# Cost of international_calls
international_calls = useful_df.query('CATEGORIA == "Internacional"')
international_calls = international_calls['VALOR'].sum().round(2)

# Cost of data_trans
data_trans = useful_df.query('CATEGORIA == "Consumo Dados"')
data_trans = data_trans['VALOR'].sum().round(2)


if analysis_number == '01':
    print('\nTotal da Conta: ', bill_cost)
    print('Descontos: ', discount)
    print('Parcelamento de Aparelhos: ', phones_installments)
    print('Assinatura Plano Voz: ', voice_plan)
    print('Serviços Gestão online: ', online_management)
    print('Tarifas Nacionais e Internacionais: ', tariffs)
    print('Outros: ', others)
    print('Local Móvel: ', local_mobile)
    print('Local Fixo: ', local_fixed)
    print('Interurbano Móvel: ', intercity_mobile)
    print('Interurbano Fixo: ', intercity_fixed)
    print('Consumo de Dados: ', data_trans)
elif analysis_number == '02':
    print('\nLocal Móvel: ', local_mobile)
    print('Local Fixo: ', local_fixed)
    print('Interurbano Móvel: ', intercity_mobile)
    print('Interurbano Fixo: ', intercity_fixed)
    print('Ligações Internacionais: ', international_calls)
elif analysis_number == '03':
    print('\nConsumo de Dados: ', data_trans)