import random

#2
array = []
for i in range(10):
    array.append(random.randint(0,11))

odd = [item for item in array if item % 2 == 1]
even = [item for item in array if item % 2 == 0]

print("original list:")
print(array)
print("odd from list:")
print(odd)
print("even from list:")
print(even)
print("\n")

#3
list = []

for i in range(10):
    list.append(random.randint(-10,1))
    
min = min(list)
max = max(list)

print("original list:")
print(list)

listenum = enumerate(list)

for i, value in listenum:
    if value < 0:
        list[i] = min
    else:
        list[i] = max

print("changed list:")
print(list)