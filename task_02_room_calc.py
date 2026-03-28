# Рассчет геометрических параметров помещения
# Исходные данные
length=float(input('Введите длину'))
width=float(input('Введите ширина'))
height=float(input('Введите высоту'))
price=125
S_floor=round(length*width,2)
S_walls=round((length+width)*2*height,2)
V=round(length*width*height,2)
# Стоимость покраски стен
cost=round(price*S_walls,2)
# Вывод результатов
print(f'Площадь пола = {S_floor} м2')
print(f'Площадь стен = {S_walls} м2')
print(f'Объем помещения = {V} м3')
print(f'Стоимость покраски стен = {cost} руб.')
