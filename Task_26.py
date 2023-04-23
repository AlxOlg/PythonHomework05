# A в степени B (рекурсия).

def power(num, exp):
    if exp > 0:
        return num * power(num, exp - 1)
    elif exp < 0:
        return 1 / power(num, -exp)
    else:
        return 1

A = int(input('Основание: '))
B = int(input('Показатель: '))
print(f'{A} ^ {B} = {power(A, B)}')
