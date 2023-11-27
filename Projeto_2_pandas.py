import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


tabela = pd.read_csv("Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores.csv")

tabela['data'] = pd.to_datetime(tabela['data'], format= '%d/%m/%Y')
tabela['precip'] = pd.to_numeric(tabela['precip'])
tabela['maxima'] = pd.to_numeric(tabela['maxima'])
tabela['minima'] = pd.to_numeric(tabela['minima'])
tabela['horas_insol'] = pd.to_numeric(tabela['horas_insol'])
tabela['temp_media'] = pd.to_numeric(tabela['temp_media'])
tabela['um_relativa'] = pd.to_numeric(tabela['um_relativa'])
tabela['vel_vento'] = pd.to_numeric(tabela['vel_vento'])
tabela['ano'] = pd.DatetimeIndex(tabela['data']).year
tabela['mes'] = pd.DatetimeIndex(tabela['data']).month

mes_usuario = 0

## Consulta de datas do item "A"##

mInicial = input('Informe o mês incial da consulta (nº): ')
mInicial = int(mInicial)
if mInicial < 1 or mInicial > 12:
    mInicial = input('Valor inválido. Informe o mês incial da consulta (nº): ')


aInicial = input('Informe o ano incial da consulta (nº): ')
aInicial = int(aInicial)
if aInicial < 1961 or aInicial > 2016:
    aInicial = input('Ano informado inválido. Informe o ano incial da consulta: ')


mFinal = input('Informe o mês final da consulta (nº): ')
mFinal = int(mFinal)
if mFinal < 1 or mFinal > 12:
    mFinal = input('Valor inválido. Informe o mês incial da consulta (nº): ')

aFinal = input('Informe o ano incial da consulta (nº): ')
aFinal = int(aFinal)
if aFinal < 1961 or aFinal > 2016:
    aFinal = input('Ano informado inválido. Informe o ano incial da consulta: ')

from datetime import date
from dateutil.relativedelta import relativedelta
from datetime import timedelta, date

dataInicial = date(aInicial,mInicial,1)

intervalo = timedelta(1)
dataFinal = date(aFinal,mFinal,1)
dataFinal = dataFinal + relativedelta(months=1)
dataFinal = dataFinal - intervalo

# ## Consulta de informações desejadas item "A"

opInfos = input('Informe o que deseja visualizar (1 = Todos os dados; 2 = Dados de precipitação; 3 = Dados de temperatura; 4 = Dados de umidade relativa e velocidade do vento. ): ')
opInfos = int(opInfos)
if opInfos < 1 or opInfos > 4:
    opInfos =  input('A opção informada não existe. Informe a opção referente aos dados que você quer visualizar')

if opInfos == 1:
    tabela = tabela.set_index(['data'])
    tabela_filt = tabela.loc[dataInicial:dataFinal]
    print(tabela_filt)

elif opInfos == 2:
    tabela = tabela.set_index(['data'])
    tabela_filt = tabela.loc[dataInicial:dataFinal, ['precip']]
    print(tabela_filt)

elif opInfos == 3:
    tabela = tabela.set_index(['data'])
    tabela_filt = tabela.loc[dataInicial:dataFinal, ['maxima','minima','temp_media']]
    print(tabela_filt)

elif opInfos == 4:
    tabela = tabela.set_index(['data'])
    tabela_filt = tabela.loc[dataInicial:dataFinal, ['um_relativa','vel_vento']]
    print(tabela_filt)

## Item "B"

precipitacao_por_mes = tabela.groupby(['ano', 'mes'])['precip'].sum().reset_index()
m_precipit = precipitacao_por_mes.loc[precipitacao_por_mes['precip'].idxmin()]
mes_precip = int(m_precipit['mes'])
ano_precip = int(m_precipit['ano'])
meses_em_portugues = {
    1: 'Janeiro',
    2: 'Fevereiro',
    3: 'Março',
    4: 'Abril',
    5: 'Maio',
    6: 'Junho',
    7: 'Julho',
    8: 'Agosto',
    9: 'Setembro',
    10: 'Outubro',
    11: 'Novembro',
    12: 'Dezembro'
}
nome_mes = meses_em_portugues.get(mes_precip) 
print(ano_precip)
print(mes_precip)
print(f"O mês com a menor quantidade de chuva foi {nome_mes}/{ano_precip} com {m_precipit['precip']} mm.")

## Item "C"


def calcular_mediastmin(tabela, mes):
    dados_filtrados = tabela[(tabela['mes'] == mes) & (tabela['ano'] >= 2006) & (tabela['ano'] <= 2016)]
    medias_por_ano = dados_filtrados.groupby('ano')['minima'].mean()
    media_geral_periodo = dados_filtrados['minima'].mean()

    return medias_por_ano, media_geral_periodo

while True:
    try:
        mes_usuario = int(input("Informe o número do mês (1 a 12): "))
        if 1 <= mes_usuario <= 12:
            break
        else:
            print("Entrada inválida. Informe um número de mês válido.")
    except ValueError:
        print("Entrada inválida. Informe um número de mês válido.")

medias_por_ano, media_geral_periodo = calcular_mediastmin(tabela, mes_usuario)

print("\nMédias da temperatura mínima para o mês de", meses_em_portugues[mes_usuario], "nos últimos 11 anos:")
for ano, media in medias_por_ano.items():
    print(f"{meses_em_portugues[mes_usuario]}/{ano}: {media:.2f} °C")

print("\nMédia geral da temperatura mínima para o período:", media_geral_periodo, "°C")


## Item "D"

def gerar_grafico_medias_temp_min(medias_por_ano, mes):
    anos = list(medias_por_ano.index)
    medias = list(medias_por_ano)

   
    plt.figure(figsize=(10, 6))
    plt.bar(anos, medias, color='blue')
    plt.title(f'Médias de Temperatura Mínima para o Mês de {meses_em_portugues[mes]} nos Últimos 11 Anos')
    plt.xlabel('Ano')
    plt.ylabel('Média de Temperatura Mínima (°C)')
    plt.xticks(anos)
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    
    plt.show()
gerar_grafico_medias_temp_min(medias_por_ano,mes_usuario)

