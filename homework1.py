from random import randint

'''2.Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей.
Дано a, b, c - стороны предполагаемого треугольника.
Требуется сравнить длину каждого отрезка-стороны с суммой двух других.
Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.
Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.'''


def is_triangle(a: int, b: int, c: int) -> {str, str | bool}:
    result = {'isTriangle': False, 'descpiption': "Введеные значения длин не подходят для треугольника"}

    result['isTriangle'] = ((a + b) >= c and (a + c) >= b and (b +c) >= a)

    if not result['isTriangle']:
        return result

    equilateralTriangle = (a == b == c)
    isoscelesTriangle = (a == b or a == c or b == c)

    result['descpiption'] = f'Треугольник равносторонний {equilateralTriangle}, треугольник равнобедренный = {isoscelesTriangle}'

    return result

a = int(input('введите сторону а треугольника '))
b = int(input('введите сторону а треугольника '))
c = int(input('введите сторону а треугольника '))

res = is_triangle(a, b, c)
for key, value in res.items():
    print(f'{key = } {value=}')

'''3. Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
 Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
 Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч'''

def is_prime_number(number):

    if not isinstance(number, int) or number < 0 or number > 100000:
        print("Необходимо ввести целое число от 1 до 100000")
        return False

    if number in (0, 1, 2):
        return True

    max_value = number
    pos = 2
    while pos < max_value:
        if number % pos == 0:
            return False
        max_value = int(round(number/pos) + 1)
        pos += 1

    return True

number = int(input('Введите число от 0 до 100000 для проверки на простоту '))
print(f'Результат проверки числа {number} на простоту: {is_prime_number(number)}')

'''5. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток.
 Программа должна подсказывать «больше» или «меньше» после каждой попытки.'''

num = randint(0, 1000)
print('Загадано случайное число')

for i in range(1, 11):
    el = int(input(f'Попытка {i}. Введите число (угадайте) '))
    if el == num:
        print('Вы отгадали число')
        break
    elif el < num:
        print('Ваше число меньше загаданного')
    else:
        print('Ваше число больше загаданного')
else:
    print("Вы не отгадали число")