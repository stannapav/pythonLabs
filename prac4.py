import math

# N.2
#a
for i in range(5):
    print(i, end=" ")
print()

#b
for i in range(5, 10):
    print(i, end=" ")
print()

#c
for i in range(1, 10, 2):
    print(i, end=" ")
print()

#d
for i in range(-2, 5):
    print(i, end=" ")
print()

#e
for i in range(100, 0, -20):
    print(i, end=" ")
print("\n")

#3
print("x | y")
for x in range(1, 11):
    y = x / (x**2 + 1)
    print(f"{x} | {y:.3f}")
print()

#4
a = int(input("enter a -> "))
b = int(input("enter a -> "))

if (b > a):
    print(f"nums from {a} - {b}")
    for i in range(a, b + 1):
        print(f"{i} | {i * 5}")

elif (a > b):
    print(f"nums from {a} - {b}")
    for i in range(a,  b - 1, -1):
        print(f"{i} | {i * 5}")
print()

#5
a = int(input("enter a -> "))
b = int(input("enter a -> "))

if (b > a):
    print(f"nums from {a} - {b}")
    for i in range(a, b + 1):
        y = 9 * math.sin(5 * i + math.pi / 3) - 4 * math.cos(7 * i + 2)
        print(f"{i} | {y:.2f}")

elif (a > b):
    print(f"nums from {a} - {b}")
    for i in range(a,  b - 1, -1):
        y = 9 * math.sin(5 * i + math.pi / 3) - 4 * math.cos(7 * i + 2)
        print(f"{i} | {y:.2f}")
print()

#6
promizok = 0.8
i = 2.5
while i >= 2.5 and i <= 9.7:
    y = (1.5 * i - math.log10(2 * i)) / (3 * i + 1)
    print(f"{i:.1f} | {y:.3f}")
    i += promizok

#7
e = float(input("enter e -> ")) # 1.4
n = 1
sum = 0
while True:
    y = (4 * n - 2) / (n * (n  + 1) * (n + 2))
    print(f"{n} | {y:.6f} | sum: {sum:.6f}")

    if y < e:
        break
    else:
        n += 1
        sum += y