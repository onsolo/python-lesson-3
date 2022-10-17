# Задача 1. Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
# 6 –> 1 1 2 3 5 8

def getFibonacci(n):
    f1 = 1
    f2 = 1

    fib = ['1', '1']
    for i in range(2, n):
        f1, f2 = f2, f1 + f2
        fib.append(str(f2))
    return fib


n = int(input('Введите длину ряда: '))
data = open('text.txt', 'w')
data.write(' '.join(getFibonacci(n)))
data.close()
