total = 0

for i in range(1, 4):
    nome = input(f"Digite o nome do produto {i}:")
    preco = float(input(f"Digite o preço unitário do produto {i}:"))
    quantidade = int(input(f"Digite a quantidade do produto {i}:"))
    
    total += preco * quantidade

print(f"Total: {total:,.2f}")