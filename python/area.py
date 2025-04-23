def get_rectangle_area(length, width):
    area = length * width
    return area

def get_rectangle_perimeter(length, width):
    perimiter = 2 * (length + width)
    return perimiter
# Длина прямоугольника.
length = 5
# Ширина прямоугольника.
width = 10

print('Площадь: ', get_rectangle_area(length, width))
print('Периметр: ', get_rectangle_perimeter(length, width))