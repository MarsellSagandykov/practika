# импорт
from math import radians, sqrt, cos

#переменные
first = float(input("длина первой стороны (см)"))
second = float(input("Введите длину второй стороны (см)"))
ugol = int(input("Введите угол между первой и второй стороной треугольника в градусах: "))

#вычисление
rad = radians(ugol)
third = sqrt(first**2 + second**2 - 2 * first * second * cos(rad))

#вывод
print("Длина третьей стороны=", third)