horas_por_mes=int(input("quantas horas voce trabalha por mes?:"))
dinheiro_hora=float(input("quanto vc recebe por hora?:"))

salario_bruto=dinheiro_hora*horas_por_mes

print("salario bruto:",salario_bruto)

INSS=salario_bruto*0.08

print("INSS:",INSS)

imposto_de_renda=salario_bruto*0.11

print("imposto de renda:",imposto_de_renda)

sindicato=salario_bruto*0.05

print("sundicato:",sindicato)

salario_liquido=salario_bruto-INSS-imposto_de_renda-sindicato

print("salario liquido:",salario_liquido)



