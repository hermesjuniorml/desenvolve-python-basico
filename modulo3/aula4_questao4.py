distancia = float(input("Digite a distância da entrega (em km): "))
peso = float(input("Digite o peso do pacote (em kg): "))

if distancia <= 100:
    preco_por_kg = 1.0
elif distancia <= 300:
    preco_por_kg = 1.5
else:
    preco_por_kg = 2.0

frete = peso * preco_por_kg

if peso > 10:
    frete += 10.0

print(f"Valor do frete: R${frete:.2f}")