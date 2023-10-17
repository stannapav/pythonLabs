#1
contries = ("Ukraine", "France", "United States", "China", "Spain", "Italy", "Turkey", "United Kingdom", "Germany", "Canada")
 
#2
while True:
    k = int(input(f"Enter index of element to look at [0 - {len(contries) - 1}] -> "))
    if k < len(contries):
        print("Wrong index please enter another")
        break

print(f"In index {k} = {contries[k]}\n")

#3
newturple = ("cat", "dog", "fish")
contries += newturple
print("Added to turple more items:")
print(contries)

print(f"\nmax: {max(contries)}")
print(f"min: {min(contries)}\n")

#4
item = input("Enter item of turple: ")

if item in contries:
    print(f"{item} is in turple")
    print(f"Index of item: {contries.index(item)}")
    print(f"Count of items: {contries.count(item)}\n")

else:
    print(f"{item} isn't in turple\n")

#5
list = list(contries)
print("list created:")
print(list)

#6
cosmicObj = ["Galaxies", "Dark Matter", "Black Holes", "Galaxies", "Binary Stars", "Clusters of Galaxies", "Dark Matter"]
print(f"\nComic objects:")
print(cosmicObj)
print()

#7
for i in range(3):
    el = input("Enter cosmic obj: ")
    cosmicObj.append(el)

print(f"\nComic objects:")
print(cosmicObj)

#8
index = int(input(f"\nEnter index 0 - {len(cosmicObj) - 1}: "))
item = input("Enter cosmic object: ")
cosmicObj.insert(index, item)
print(cosmicObj)
print()

#9
items = []
for i in range(3):
    item = input("Enter item to add in list: ")
    items.extend(item)

print(items)

#10
copy = items.copy()
item = input("\nEnter item to look in list: ")

if item in items:
    print(f"{item} is in list")
    print(f"Index of item: {items.index(item)}")
    print(f"Count of items: {items.count(item)}\n")

else:
    print(f"{item} isn't in list\n")

#11
items.sort()
print("Sorted list:")
print(items)

items.reverse()
print("\nReverst list:")
print(items)

#1
item = input("\nEnter item to remove from list: ")

if item in items:
    items.remove(item)
    print("Item removed")
    print(items)
    print()

else:
    print(f"{item} isn't in list\n")

#13
print("Delete first 2 el")
del items[:2]
print(items)
print(f"lenght of list: {len(items)}\n")

print("Delete last 2 el")
del items[(len(items) - 2) : ]
print(items)
print(f"lenght of list: {len(items)}\n")

print("Delete odd el")
del items[ 1 : : 2]
print(items)
print(f"lenght of list: {len(items)}\n")

#14
print("Print list item by item form list:")
print(copy)
for item in copy:
    print(item)
print()

#15
for i in copy:
    if copy.count(i) > 1:
        copy.remove(i)

print("list without duplicates")
print(copy)

tuple = tuple(copy)
print("\nCreated tuple from list")
print(tuple)