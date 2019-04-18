
import re
import random
import json

Country = []
City = []
Street = []
Test = ["Test"]
path = "base.json"

def check(locname):
    """
    Функция проверки наименования, страны, города улицы на отсутствие лишних символов
    """
    checkattemp = re.fullmatch(r'[a-z0-9A-Z- ]+', locname)
    if bool(checkattemp) is not True:
        raise NameError("Неверный формат данных")
    return locname

def beautycoat(word):
    def beautydress(func):
        def wrapper(*args, **kwargs):
            if args == "Test":
                print(f"Вызов функции {func} с параметрами {args}")
                raise NameError("Неверный аргумент функции")
            if kwargs == "Test":
                print(f"Вызов функции {func} с параметрами {kwargs}")
                raise NameError("Неверный аргумент функции")
            result = func(*args)
            return result
        return wrapper
    return beautydress

#@beautydress
def locationgenerator(Country, City, Street):
    while True:
        RndmCountry = random.choice(Country)
        RndmCity = random.choice(City)
        RndmStreet = random.choice(Street)
        RndmHouseNum = random.randint(1, 100)
        # LiterNum = random.randint(1, 5)
        # RndmLitera = random.choice("", LiterNum)
        RndmFlat = random.randint(1, 500)
        yield RndmCountry, RndmCity, RndmStreet, RndmHouseNum, RndmFlat
    #   print(f"{RndmCountry}, {RndmCity}, {RndmStreet}, house:{RndmHouseNum}, flat:{RndmFlat}")

with open(path, "r") as f:
    data = json.loads(f.read())
    for i in data["Country"]:
        check(i)
        Country.append(i)
    for i in data["City"]:
        check(i)
        City.append(i)
    for i in data["Street"]:
        check(i)
        Street.append(i)

newloc = locationgenerator(Country, City, Street)

print(next(newloc))
print(next(newloc))
print(next(newloc))
print(next(newloc))

newloc2 = locationgenerator(Country, City, Test)

print(next(newloc2))
print(next(newloc2))
print(next(newloc2))
print(next(newloc2))

