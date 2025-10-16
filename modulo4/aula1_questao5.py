print(" # # Inicio programa de cálculo das idades # # ")
n=int(input("Insira a quantidade de participantes: "))
soma=0
contador=0
while (contador < n):
    nota=int(input(f"Insira a idade do {contador+1}º participante: "))
    soma=soma+nota
    contador+=1
print(f"A média das idades é: {(soma//n)}")
