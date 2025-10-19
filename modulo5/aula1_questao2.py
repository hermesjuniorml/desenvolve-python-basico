import math
import random

x=int(input("Quantos numeros quer? "))
soma=0
for i in range(x):
    soma+=random.randint(0,100)

print(f"{math.sqrt(soma)}")