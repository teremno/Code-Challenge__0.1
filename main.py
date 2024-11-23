# Практика  1 уровень: 1, 2, 3, 4
# 1
'''
a = int(input('Ведіть число: '))
b = int(input('Ведіть число: '))
print(a ** b)

# 2

day = int(input('Ведіть число від 1 до 7: '))
if day == 1:
    print('Понеділок')
elif day == 2:
    print('Вівторок')
elif day == 3:
    print('Середа')
elif day == 4:
    print('Четвер')
elif day == 5:
    print('Пятниця')
elif day == 6:
    print('Субота')
elif day == 7:
    print('Неділя')
else:
    print('Ви хочете більше часу, на жаль його нема. Цінуйте час, який ще є!')

# 3

number1 = int(input('Введіть число: '))
number2 = int(input('Введіть число: '))
if number1 > number2:
    print(number1)
else:
    print(number2)

# 4

_deposit_usd = float(input('Введіть свій депозит в USD: '))
_kurs_uah_usd = float(input('Введіть курс USD до UAH: '))
your_depo = _deposit_usd * _kurs_uah_usd
print('Ваш депозит у гривнях ' + str(your_depo))

# 2 уровень: 1, 2, 3
# 1

_user_number = int(input('Введіть число: '))
if _user_number % 2 == 0:
    print('Парне число')
else:
    print('Непарне число')

# 2

_numb_user_1 = int(input('Введіть число: '))
_numb_user_2 = int(input('Введіть число: '))
_numb_user_3 = int(input('Введіть число: '))

if _numb_user_1 > _numb_user_2 and _numb_user_1 > _numb_user_3:
    print(_numb_user_1, 'Це найбільше число')
elif _numb_user_2 > _numb_user_3:
    print(_numb_user_2, 'Це найбільше число')
else:
    print(_numb_user_3, 'Це найбільше число')

# 3

_min_sleep_ = int(input('Мінімальни час сну? '))
_max_sleep_ = int(input('Максимальний час сну? '))
_time_sleep_ = int(input('Скільки часу ви спите? '))

if _time_sleep_ < _min_sleep_:
    print('Ви спите не достатньо!')
elif _time_sleep_ > _max_sleep_:
    print('Ви спите забагато!')
else:
    print('Ви спите добре!')

# 3 уровень: 1, 2, 3

# 1

_num_1 = float(input('Ввести число: '))
_num_2 = float(input('Ввести число: '))
_math_simbol = input('Ввдіть символ: (+, -, /, *, mod, pow, div) ')

if _math_simbol == '+':
    result = _num_1 + _num_2

elif _math_simbol == '-':
    result = _num_1 - _num_2

elif _math_simbol == '/':
    if _num_2 != 0:
        result = _num_1 / _num_2
    else:
        result = 'Ділення на нуль'
elif _math_simbol == '*':
    result = _num_1 * _num_2

elif _math_simbol == 'mod':
    if _num_2 != 0:
        result = _num_1 % _num_2
    else:
        result = 'Ділення на нуль'

elif _math_simbol == 'pow':
    result = _num_1 ** _num_2

elif _math_simbol == 'div':
    if _num_2 != 0:
        result = _num_1 // _num_2
    else:
        result = 'Ділення на нуль'

else:
    result = 'Не вірний формат введення'

print('Результат ', result)

# 2

_num_1 = int(input('Введіть чисо: '))
_num_2 = int(input('Введіть чисо: '))

if _num_2 != 0:
    if _num_1 % _num_2 == 0:
        print(f'{_num_1} Ділиться на {_num_2} без остачі')
    else:
        print(f'{_num_1} Не ділиться на {_num_2} без остачі')

else:
    print(f'Ділення не можливе для {_num_1} і {_num_2}')

if _num_1 != 0:
    if _num_2 % _num_1 == 0:
        print(f'{_num_2} Ділиться на {_num_1} без остачі')
    else:
        print(f'{_num_2} Не ділиться на {_num_1} без остачі')

else:
    print(f'Ділення не можливе для {_num_2} і {_num_1}')

# 3

_num_ = int(input('Введіть трьохзначне число: '))
if 100 <= _num_ <= 999:
    _num1 = _num_ // 100
    _num2 = (_num_ // 10) % 10
    _num3 = _num_ % 10

    if _num1 == _num2 or _num1 == _num3 or _num2 == _num3:
        print('Збіг знайдено!')

    else:
        print('Збігів не знайдено')

else:
    print('Не правильне введення!')'''


