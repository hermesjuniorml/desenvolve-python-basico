import random
num_elementos=random.randint(5,20)
elementos=[random.randint(1,10) for i in range(num_elementos)]
print(elementos)
print(sum(elementos))
print(sum(elementos)/len(elementos))