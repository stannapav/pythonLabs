#1
contries = ("Ukraine", "France", "United States", "China", "Spain", "Italy", "Turkey", "United Kingdom", "Germany", "Canada")
 
#2
while True:
    k = int(input(f"Enter index of element to look at [0 - {contries.__len__() - 1}] -> "))
    if k < contries.__len__():
        print("Wrong index please enter another")
        break

print(f"In index {k} = {contries[k]}")

#3
newturple = ("cat", "dog", "fish")
contries += newturple
print("Added to turple more items:")
print(contries)