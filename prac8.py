import random

n = int(input("Enter matrix NxN what n: "))
array2D = [[0] * n for i in range(n)] 

for i in range(n):
    for j in range(n):
        array2D[i][j] = random.randint(0, (n - 1) * 2)

print("2D array:")
for i in range(n):
        print(array2D[i])       

print("\nelements that equal their sum of i and j:")
for i in range(n):
    for j in range(n):
        if array2D[i][j] == i + j:
            print(f"idex: ({i}, {j}) num: {array2D[i][j]}")