#2
print("2) made dictionary")
colors = {
    "red" : "#FF0000",
    "green" : "#008000",
    "blue" : "#0000FF",
    "yellow" : "#FFFF00",
    "purple" : "#800080",
    "white" : "#FFFFFF",
    "black" : "#000000",
    "orange" : "#FFA500",
    "lavander" : "#E6E6FA",
    "pink" : "#FFC0CB"
}

for key in colors:
    print(f"{key} : {colors.get(key)}")

print(f"lenght : {len(colors)}")
print('\n')

#3
print("3) looking at specific el")
color = input("enter name of color that you want to look at hex code ->")

if colors.get(color) != None:
    print(f"hex code for '{color}' is {colors.get(color)}")
else:
    print(f"sorry we dont have info for '{color}'")
print('\n')

#4
print("4) sorted dictionary")
sortedColors = dict(sorted(colors.items()))

"""
sortedColorsTurplet = sorted(colors.items())

sortedColors = {}
for key, value in sortedColorsTurplet:
    sortedColors[key] = value
"""

for key, value in sortedColors.items():
    print(f"{key}: {value}")

print('\n')

#5
print("5) printing through for key, value")

for key, value in colors.items():
    print(f"{key}: {value}")
print('\n')

#6
print("6) deleting element")
color = input("enter name of color that you want to delete->")

if colors.get(color) != None:
    del colors[color]
    print(f"'{color}' is deleted")
    for key, value in colors.items():
        print(f"{key}: {value}")
    print(f"lenght: {len(colors)}")
else:
    print(f"we dont have '{color}'")
print('\n')

#7
print("7) updating dictionary")
addColors = {"brown" : "#964B00", "grey" : "#808080", "aqua" : "#00FFFF"}
colors.update(addColors)
copyColors = colors.copy()

for key, value in copyColors.items():
    print(f"{key}: {value}")

print(f"lenght: {len(copyColors)}")
print('\n')

#8
print("8) from list to dictionary")
cosmicObj = ["Galaxies", "Dark Matter", "Black Holes", "Galaxies", "Binary Stars", "Clusters of Galaxies", "Dark Matter"]
dictionary = dict.fromkeys(cosmicObj, 666)

for key, value in dictionary.items():
    print(f"{key}: {value}")