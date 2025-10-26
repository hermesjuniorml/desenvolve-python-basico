import random

lista = [random.randint(-10, 10) for i in range(20)]

print("Lista original:")
print(lista)

inicio = fim = 0
maior_seq_ini = maior_seq_fim = 0
tamanho_atual = maior_tamanho = 0

for i, num in enumerate(lista):
    if num < 0:
        if tamanho_atual == 0:
            inicio = i
        tamanho_atual += 1
        fim = i
        if tamanho_atual > maior_tamanho:
            maior_tamanho = tamanho_atual
            maior_seq_ini, maior_seq_fim = inicio, fim
    else:
        tamanho_atual = 0
if maior_tamanho > 0:
    del lista[maior_seq_ini:maior_seq_fim + 1]

print("Lista após deletar o intervalo com mais números negativos consecutivos:")
print(lista)
