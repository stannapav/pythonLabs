#1
def primeNum(start, end):
    for num in range(start, end + 1):
        if num > 1 and (num % 2 != 0 or num == 2) and (num % 3 != 0 or num == 3):
            print(num, end = " ")

primeNum(1,101) 
print('\n')

#2
words = ["hi", "wassup", "cats", "nice"]
func = lambda word: word.title() + '!'

newWords = list(map(func, words))

print(newWords)