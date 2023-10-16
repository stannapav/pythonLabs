import string
import nltk_stopwords

readFile = open("catStory.txt", "r")
catStory = readFile.read()
print("Text:")
print(catStory)
print("\n")

catStory = catStory.replace("'", " ")
for char in string.punctuation:
    catStory = catStory.replace(char, "")

for char in string.digits:
    catStory = catStory.replace(char, "")

catStory = catStory.casefold()

words = catStory.split()
stopwords = nltk_stopwords.stopwords()
wordsFiltered = [word for word in words if word not in stopwords]

frequencyDictionary = {}

for word in wordsFiltered:
    if word in frequencyDictionary:
        frequencyDictionary[word] += 1
    else:
        frequencyDictionary[word] = 1

print("sorted by key:")
sortedByKey = sorted(frequencyDictionary.items())
for key, value in sortedByKey:
    print(f"{key:15}: {value:2}")
print("\n")

print("sorted by value:")
sortedByValue = [(frequencyDictionary[key],key) for key in frequencyDictionary] 
sortedByValue = sorted(sortedByValue, reverse=True)
for key, value in sortedByValue:
    print(f"{key}: {value}")