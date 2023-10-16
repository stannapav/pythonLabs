#2
print("2) slicing str")
str = "My alphabet starts where your alphabet ends."
slicedStrings = []

slicedStrings.append(str[3 : 10])
slicedStrings.append(str[3 : -2])
slicedStrings.append(str[0 : 1])
slicedStrings.append(str[-1 : 1])
slicedStrings.append(str[ : 17])
slicedStrings.append(str[18 : ])

index = 1
for string in slicedStrings:
    print(f"{index}: {string}")
    index +=  1
print('\n')

#4

print("3) num and letters")
numAndAlphabet = "abc123"
spaceIsThere = "abc 123"

print(numAndAlphabet.isalnum())
print(spaceIsThere.isalnum())
print('\n')

#5
print("5) letters")
withoutNum = "coolNick"
withNum = "coolNick666"

print(withoutNum.isalpha())
print(withNum.isalpha())
print('\n')

#6
print("6) nums")
allNum = "666"
numAndLetters = "cool num 666"

print(allNum.isdigit())
print(numAndLetters.isdigit())
print('\n')

#7
print("7) upper")
upper = "AAAAAAAA"
notUpper = "AaAaAa"

print(upper.isupper())
print(notUpper.isupper())
print('\n')

#8
print("8) lower")
lower = "hehehehe"
notLower = "hEhEhE"

print(lower.islower())
print(notLower.islower())
print('\n')

#9
print("9) find start and end index")
catFacts = """Cats are believed to be the only mammals who don’t taste sweetness.
Cats are nearsighted, but their peripheral vision and night vision are much better than that of humans.
Cats are supposed to have 18 toes (five toes on each front paw; four toes on each back paw)."""

print(catFacts)
substr = input("enter substr from text above: ")

startIndex = catFacts.find(substr)
endIndex = catFacts.rfind(substr)

if startIndex == -1 and endIndex == -1:
    print(f"there is no '{substr}'")
elif startIndex == endIndex:
    print(f"there is only one '{substr} and it's index: {startIndex}'")
else:
    print(f"first index: {startIndex}, last: {endIndex}")
print('\n')

#10
print("10) find all indexs")
pos = -1
print(f"all indexs of '{substr}':", end = " ")
while True:
    pos = catFacts.find(substr, pos + 1)

    if pos == -1 : break

    print(pos, end = " ")
print('\n')

#11
print("11) starts, ends with this substr")
substr = input("input substring that text above strats with: ")
print(f"it's {catFacts.startswith(substr)}")

substr = input("input substring that text above ends with: ")
print(f"it's {catFacts.endswith(substr)}")