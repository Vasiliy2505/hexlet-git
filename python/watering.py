# Опишите параметры функции calculate_watering().
def calculate_watering(plant_type, number_of_plants, volume_per_plant=2.5):
    # Здесь вместо ellipsis напишите код функции.
    result = number_of_plants * volume_per_plant
    print(plant_type, number_of_plants, 'шт.: для полива требуется', result, 'л воды.' ) 

# Не изменяйте код ниже этого комментария: 
# если ваша функция написана правильно - эти вызовы должны успешно сработать.

# Вызов функции с позиционными аргументами:
calculate_watering('Артишоки', 20, 4)

# Вызов функции с позиционными аргументами, без опционального:
calculate_watering('Кивано', 15)

# Вызов функции с именованными аргументами, без опционального:
calculate_watering(number_of_plants=15, plant_type='Тыквы')