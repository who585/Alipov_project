# Прайс лист матераилов
# Исходные данные
materials = {
"Кирпич": 585, 
"Бетон": 171, 
"Штукатурка": 6767,
"Металл": 666,
"Стекло": 58571                                           
}
# Добавление материалов
materials.update({
    "Черепица": 1000,
    "Фарфор": 2000
})
# Измененеие цены
materials["Кирпич"] *= 1.1
materials.pop("Фарфор")
# Расчет средней цены
average = sum(materials.values())/len(materials)
print(materials)
print(average)
