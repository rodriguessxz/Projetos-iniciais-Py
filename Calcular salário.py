
# Solicita o salário por hora e o número de horas trabalhadas por mês
hora = float(input('Quanto ganha por hora? ')) 
horas_mes = float(input('Quantas horas trabalha por mês? '))

# Calcula o salário bruto
total = hora * horas_mes
salario_bruto = total

# Calcula os descontos
imposto_renda = total * 0.11  # 11% de imposto de renda
inss = total * 0.08  # 8% de INSS (correção de 0.8 para 0.08)
sindicato = total * 0.05  # 5% de sindicato (correção de 0.5 para 0.05)
descontos = imposto_renda + inss + sindicato

# Calcula o salário líquido
salario_liquido = total - descontos

# Imprime os resultados
print('O salário bruto é: R$: ') 
print(salario_bruto)

print('Os descontos são de: R$') 
print(descontos)

print('O salário líquido é: R$ ') 
print(salario_liquido)

