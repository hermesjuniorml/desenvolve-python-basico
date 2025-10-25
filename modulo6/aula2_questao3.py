import random
lista1=[random.randint(0,50) for i in range(20)]
lista2=[random.randint(0,50) for i in range(20)]
print(f"Lista 1 - {lista1}")
print(f"Lista 2 - {lista2}")
intersec=list(set(lista1) & set(lista2))

print(f"Intersecção - {intersec}")
for i in intersec:
    print(f"{i}:(lista1={lista1.count(i)}, lista2={lista2.count(i)})")