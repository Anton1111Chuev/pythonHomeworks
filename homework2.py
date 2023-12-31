import math

'''Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.'''
def by_number_system(number:int, basis:int = 16):
    result = []
    div = number
    dict = {10: 'a', 11: 'b', 12: 'c', 13:'d', 14: 'e', 15: 'f'}
    while div >= basis:
        div, mode = divmod(div, basis)
        result.append(dict.get(mode, str(mode)))
    result.append(dict.get(div, str(div)))
    result.reverse()
    return ''.join(result)

num = int(input('Введите целое число для перевода в 16-ичную систему '))
print(f'Число в 16-ичной системе {by_number_system(num)}, контроль {hex(num)}')

'''Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.'''

def fraction():
    def str_in_numerator_denominator(text: str) -> list:
        res = text.split('/')
        if len(res) != 2 or not res[0].isnumeric() or not res[1].isnumeric() or res[1] == '0':
            raise Exception('Вид вводимых данных должен быть a/b где а и в это числа знаменатель не должен быть = 0')

        res[0] = int(res[0])
        res[1] = int(res[1])
        return res

    def cut_fraction(numerator, denominator) -> str:
        if numerator % denominator == 0:
            return (f'{numerator / denominator} ')

        gcd = math.gcd(numerator, denominator)
        if gcd > 1:
            numerator /= gcd
            denominator /= gcd

        return (f'{int(numerator)}/{int(denominator)}')

    str1 = input('Введите первую строку вида “a/b” ')
    str2 = input('Введите вторую строку вида “a/b” ')

    try:
        fraction1 = str_in_numerator_denominator(str1)
        fraction2 = str_in_numerator_denominator(str2)
    except Exception as e:
        print(f'Продолжение выполнения не возможно {e}')
        return

    denominator = fraction1[1] * fraction2[1]
    sum_numerator = fraction1[0] * fraction2[1] + fraction2[0] * fraction1[1]
    milt_numerator = fraction1[0] * fraction2[0]
    print(f"Произведение дробей {str1} и {str2} равно {cut_fraction(milt_numerator, denominator)}")
    print(f"Сумма дробей {str1} и {str2} равна {cut_fraction(sum_numerator, denominator)}")


fraction()
