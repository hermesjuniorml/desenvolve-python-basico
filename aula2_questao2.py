
frase=str(input("Digite uma frase: "))
asterisco = lambda fras:"".join(([letra if letra.lower() not in ['a','e','i','o','u'] else '*' for letra in fras]))
list_frase=list(map(asterisco, frase))
frase_mod="".join(list_frase)
print(f"Frase modificada: {frase_mod}")
