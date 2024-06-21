def decimal_to_any(number, notation=2):  # рекурентная функция перевода числа из деситичной в любую
    if number < notation:                 # систему счисления, по умолчанию в вторую
        return str(number)
    else:
        return str(decimal_to_any(number // notation, notation)) + str(number % notation)


def int_input_check():  # проверка правильности ввода пользователя
    try:
        number = int(input('Введите целое не отрицательное число\n'))
    except ValueError:
        print('Вы ввели не целое число')
        return
    if number < 0:
        print('Вы ввели отрицательное число')
        return
    return number


def convertors_start(number, notation=2):  # костыль чтобы не делать цикл и не выключать программу в ручную
    try:                                    # на случай если пользователь не знает какое число надо ввести
        print(decimal_to_any(number, notation))
    except TypeError:
        print('Запустите программу ещё раз с другими данными')
