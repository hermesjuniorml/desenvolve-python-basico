import random
nomes = ["Luana", "Ju", "Davi", "Vivi", "Pri", "Luiz"]
# chave_aleatoria = 5
# nomes_cript = ['Qzfsf', 'Oz', 'If{n', '[n{n', 'Uwn', 'Qzn!']

def encrypt(lista_nomes):
    nomes_encryptados = []
    chave_aleatoria=random.randint(1,10)
    for nome in lista_nomes:
        nome_encryptado=[str(" ")]
        for letra in nome:
            unicode_str=ord(letra)+chave_aleatoria
            if(unicode_str > 126):
                unicode_str=(unicode_str%126)+33
            nome_encryptado.append(chr(unicode_str))
        nomes_encryptados.append("".join(nome_encryptado))
    return (nomes_encryptados, chave_aleatoria)

[nomes_cript, key_aleatoria]= encrypt(nomes)
print(f"nomes = {nomes}", f"chave_aleatoria = {key_aleatoria}")
    