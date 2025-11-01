import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []

    for palavra in palavras:
        if len(palavra) <= 3:
            nova_frase.append(palavra)
        else:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            palavra_embaralhada = palavra[0] + ''.join(meio) + palavra[-1]
            nova_frase.append(palavra_embaralhada)

    return ' '.join(nova_frase)

frase = "Python é uma linguagem de programação"
resultado = embaralhar_palavras(frase)
print(resultado)
