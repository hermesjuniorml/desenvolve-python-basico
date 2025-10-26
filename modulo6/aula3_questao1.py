numeros = []

print("Digite números inteiros (digite 'sair' para encerrar):")

while True:
    entrada = input("Número: ")
    if entrada == 'sair':
        break
    numero = int(entrada)
    numeros.append(numero)
if len(numeros) < 4:
    print("\nVocê precisa informar pelo menos 4 números!")
else:
    print("\n=== Resultados ===")
    print(f"Lista original: {numeros}")
    print(f"3 primeiros elementos: {numeros[:3]}")
    print(f"2 últimos elementos: {numeros[-2:]}")
    print(f"Lista invertida: {numeros[::-1]}")
    print(f"Elementos de índice par: {numeros[::2]}")
    print(f"Elementos de índice ímpar: {numeros[1::2]}")