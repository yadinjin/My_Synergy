print('Введите через пробел длины сторон прямоугольника в см:')
a, b = map(float, input().split())
print("Площадь прямоугольника = ", a*b, " кв. см")
print("Периметр прямоугольника = ", 2*(a+b)," см")