#4.9. Визначити вартість дзвінка по телефону. Ціна за хвилину розмови 2,30 грн. По суботам та неділям надається знижка 20%.
from enum import Enum
 
class DaysOfWeek(Enum):
    Monday = 1
    Thuesday = 2
    Wednesday = 3
    Thursday = 4
    Friday = 5
    Saturday = 6
    Sunday = 7

oneMinute = 2.3
minutes = int(input("Введіть скільки хвилин була телефоний дзвінок -> "))

while True:
    day = int(input("Введіть день тижня(пн - 1, вт - 2, ср - 3, чт - 4, пт - 5, сб - 6. нд - 7) -> "))
    if day >= 1 and day <= 7:
        break

    print("Такого значення нема")

if day == DaysOfWeek.Saturday.value or day == DaysOfWeek.Sunday.value:
    price = ((oneMinute * minutes) / 100) * 80
    print(f"У вас знижка 20% тому усьо ціна: {price:.2f} гривень")
else:
    price = oneMinute * minutes


#5.9. Написати програму, в якій при введенні часу доби виводиться відповідне привітання.
while True:
    hour = int(input("Введіть годину дня -> "))
    if hour >= 0 and hour <= 24:
        break

    print("Невірне значення")

if hour < 6:
    print("Доброї ночі")
elif hour <= 10:
    print("Доброго ранку")
elif hour <= 16:
    print("Доброго дня")
elif hour < 22:
    print("Доброго дня")
else:
    print("Надобраніч")