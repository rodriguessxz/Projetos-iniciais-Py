# Peso máximo permitido (em kg)
peso_maximo = 80

# Peso real (em kg)
peso_real = 85

# Calcula o excesso de peso
excesso_peso = peso_real - peso_maximo

# Verifica se há excesso de peso e calcula a multa
if excesso_peso > 0:
    multa_por_kg = 4  # Valor da multa por kg excedente
    multa = excesso_peso * multa_por_kg
    print(f"Excesso de peso: {excesso_peso} kg")
    print(f"Multa a ser paga: R${multa:.2f}")
else:
    multa = 0
    print("Não há excesso de peso.")
    print("Sem multa.")

# Exibe o valor armazenado na variável multa
print(f"Valor da multa registrado: R${multa:.2f}")
