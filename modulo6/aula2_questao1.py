import random
list=[]
for i in range(20):
    list.append(random.randint(-100,100))

print(sorted(list))
print(list)
print(list.index(max(list)))
print(list.index(min(list)))