# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
from decimal import Decimal, getcontext
# Из модуля math импортируйте константу "пи".
from math import pi


# Установите необходимую точность для вычислений.
getcontext().prec = 10

# Приведите константу "пи" к типу Decimal.
# Помните, что Decimal() принимает строку, а константа "пи" - это число.
pi = Decimal(str(pi))

# Функция get_ellipse_area() должна принимать два параметра:
# размер длинной и короткой полуоси.
def get_ellipse_area(long_axis,short_axis):
    return pi * long_axis * short_axis
     
    # Вычислите площадь эллипса на основе переданных в функцию
    # значений полуосей.
    # Верните получившееся значение (площадь эллипса).


# Объявите три переменные типа Decimal.
long_axis = Decimal('2.5')  # Длинная полуось эллипса.
short_axis = Decimal('1.75')  # Короткая полуось эллипса.
depth = Decimal('0.35')  # Глубина пруда.


# Вызовите функцию get_ellipse_area(), в аргументах передайте длины полуосей эллипса.
# Результат работы функции присвойте переменной area:
area = get_ellipse_area(long_axis,short_axis)

# Вычислите объём пруда: умножьте площадь на глубину.
volume = area * depth

# Напечатайте фразы с результатами вычислений.
print('Площадь пруда:', area,'кв.м.')  # Должно быть напечатано: Площадь пруда: <значение> кв.м.
print('Количество воды для наполнения пруда:', volume,'куб.м.')  # Должно быть напечатано: Количество воды для наполнения пруда: <значение> куб.м