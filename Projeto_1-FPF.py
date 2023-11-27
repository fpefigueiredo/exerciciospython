ind_meses = [1,2,3,4,5,6,7,8,9,10,11,12]
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
temperaturas = []
md_anual = 0
m_max = 0
m_min = 0

### enquanto m<12, aparece a solicitacao de input e armazena numa variavel t(cont)

i = 0
meses_maior38 = 0
temp_max = -60
temp_min = 50

while i < len(meses):
    t = float(input(f"Informe a temperatura do mês de {ind_meses[i]}: "))
   
    while t < -60 or t > 50:
        print ('Valor inválido, informe novamente')
        t = float(input(f"Informe a temperatura do mês {ind_meses[i]}: "))
    md_anual = md_anual + t
    temperaturas.append(t)

    if t > 38:
        meses_maior38 = meses_maior38 + 1
    
    if temp_max < t:
        temp_max = t

    if temp_min > t:
        temp_min = t

    i = i + 1
md_anual = (md_anual/12)

m_max = temperaturas.index(temp_max)
m_min = temperaturas.index(temp_min)

print('A temperatura média máxima anual é', md_anual,'°C')
print('A quantidade de meses escaldantes (temperatura acima de 38°C) é', meses_maior38)
print('A temperatura máxima atingida neste ano é', temp_max,'°C no mês de', meses[m_max])
print('A temperatura mínima atingida neste ano é', temp_min,'°C no mês de', meses[m_min])

