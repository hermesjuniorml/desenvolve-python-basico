
while True:
    frase = input('Digite uma frase (digite "fim" para encerrar): ')
    if frase.lower() == "fim":
        break
    limpa = ''.join(c.lower() for c in frase if c.isalpha())

    if limpa == limpa[::-1]:
        print(f'\n"{frase}" é palíndromo\n')
    else:
        print(f'\n"{frase}" não é palíndromo\n')