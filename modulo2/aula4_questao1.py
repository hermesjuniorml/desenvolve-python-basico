# Lê comprimento do terreno
comprimento = int(input("Insira o comprimento do terreno: "))

# Lê a largura do terreno
largura = int(input("Insira a largura do terreno: "))

#Lê o preço do metro quadrado

preco_m2=float(input("Insira o valor do m2: "))

#calcula a área do terreno
area_m2 = comprimento * largura

# preço total do terreno
preco_total = preco_m2 * area_m2

# imprime na tela os resultados formatados

print(f"O terreno possui {area_m2}m2 e custa R${preco_total:,.2f}")