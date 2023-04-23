# Сумма двух целых чисел (рекурсия).

def sum(a, b):
    if a > 0:
        return sum(a - 1, b + 1)
    elif a < 0:
        return sum(a + 1, b - 1)
    else:
        return b

A = int(input('Первое слагаемое: '))
B = int(input('Второе слагаемое: '))
print(f'Сумма: {sum(A, B)}')
