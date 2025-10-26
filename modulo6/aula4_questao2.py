# Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase (remova espaços em branco)
# Digite uma frase: Eu gosto de programar em Python
# Vogais: ['a', 'a', 'e', 'e', 'o', 'o', 'o', 'o', 'u']
# Consoantes: ['E', 'g', 's', 't', 'd', 'p', 'r', 'g', 'r', 'm', 'r', 'm', 'P', 'y', 't', 'h', 'n'] isso ta errado kkkk

frase=str(input("Digite uma frase: "))
vogais=[letra for letra in frase if (letra.lower() in ['a','e','i','o','u'])]
print(f"Vogais: {vogais}")
consoantes=[cons for cons in frase if (cons.lower() not in vogais and cons != ' ')]
print(f"Consoantes: {consoantes}")