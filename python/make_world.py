# Код этой функции не меняйте.
def count_tiles(dep, leng, wid=None):
    if wid is None:
        wid = leng

    short_sides = 2 * wid * dep
    long_sides = 2 * leng * dep
    bottom = leng * wid
    total = short_sides + long_sides + bottom

    return total


# Допишите код функции.
def make_word(count):
    if count != 11 and count % 10 == 1:
        return 'плитка'
    elif 11 < count < 15:      # Блоков elif может быть сколько угодно.
        return 'плиток'
    elif 1 < count % 10 < 5:
        return 'плитки'     
    else :
        return 'плиток'


# Вычисляем количество плиток:
total_tiles = count_tiles(2, 2,7)

# Полученное число передаём в make_word(),
# чтобы подобрать нужное склонение для слова "плитка":
correct_word = make_word(total_tiles)

# Печатаем итоговую фразу, в которой применяем число плиток total_tiles
# и слово "плитка" в правильном склонении (correct_word):
print('Потребуется', total_tiles, correct_word)