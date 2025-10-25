lista1=[]
num_elem1=int(input("Digite a quantidade de elementos da lista 1: "))
print(f"Digite os 4 elementos da lista 1:")
for i in range(num_elem1):
    x=int(input())
    lista1.append(x)
lista2=[]

num_elem2=int(input("Digite a quantidade de elementos da lista 2: "))
print(f"Digite a quantidade de elementos da lista 2:")
for i in range(num_elem2):
    x=int(input())
    lista2.append(x)

lista_intercalada=[]
print(f"Lista intercalada:", end=" ")
for i in range(max(num_elem2, num_elem1)):
    if(i < len(lista1)):
        print(lista1[i], end=" ")
    if (i < len(lista2)):
        print(lista2[i], end=" ")
print()