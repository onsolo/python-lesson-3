# Задача 3. Создайте скрипт бота, который находит ответы на фразы по ключу в словаре. Бот должен, как минимум,
# отвечать на фразы «привет», «как тебя зовут». Если фраза ему неизвестна, он выводит соответствующую фразу.
# «как тебя зовут?» –> меня зовут Анатолий

phrases = {
    'привет': 'Привет!',
    'как тебя зовут?': 'Меня зовут Анатолий',
    'как у тебя дела?': 'Всё отлично!'
}


def getAnswer(phrase):
    if phrases.get(phrase.lower()) is None:
        return 'Такая фраза мне не известна('
    else:
        return phrases.get(phrase.lower())


phrase = input('Скажите что-нибудь: ')
print(getAnswer(phrase))
