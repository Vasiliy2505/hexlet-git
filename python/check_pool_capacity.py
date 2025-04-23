# Вместо многоточия укажите параметры num, leng и wid.
# Параметру wid присвойте значение по умолчанию.
def check_pool_capacity(num,leng,wid=None):
    if wid == 0:
        return False
    elif leng == 0:
        return False    
    elif wid == None:
        area_1 = (abs(leng) * abs(leng))
        if (abs(num) / area_1) <= 2:
            return True
        else:
            return False    
    elif wid != None:
        area_2 = (abs(leng) * abs(wid))
        if (abs(num) / area_2) <= 2:
            return True
        else:
            return False         


    


# Проверьте параметр num на отрицательное значение.

# Проверьте параметр leng на отрицательное значение.

# Проверьте значение параметра wid.

# Вычислите площадь бассейна и проверьте,
# помещаются ли в бассейне все люди из очереди.
# Верните True или False в зависимости от результата проверки.


# Код ниже полностью рабочий, он вам пригодится для проверки вашей работы.

# Функция, которая принимает на вход True или False
# и печатает текстовое сообщение.
def show_result(is_ok):
    if is_ok:  # Если передано True:
        print('Все люди из очереди поместятся в бассейн.')
    else:  # Если передано False:
        print('Люди из очереди не поместятся в бассейн.')


# Вызываем check_pool_capacity() с двумя аргументами.
# Этот вызов должен вернуть True (4 чел. в бассейн 2х2).
is_capacity_ok = check_pool_capacity(4, 2)
# Передаём результат вызова на вход show_result()
show_result(is_capacity_ok)

# Вызываем check_pool_capacity() с тремя аргументами.
# Этот вызов должен вернуть False (25 чел. в бассейн 5х2).
is_capacity_ok = check_pool_capacity(25, 5, 2)
# Передаём результат вызова на вход show_result()
show_result(is_capacity_ok)

# При необходимости добавьте свои вызовы аналогичным образом.