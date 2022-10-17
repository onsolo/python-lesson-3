# Задача 2. В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
# а –> абрикос, авокадо, апельсин, айва.

data = open('fruits.txt', encoding='UTF-8')
text = data.readlines()
data.close()


def getFruitByChar(letter):
    for i in text:
        if letter == i[0].lower():
            print(i, end='')


letter = input('Введите букву: ')
getFruitByChar(letter)
