# Использование множеств для анализа материалов трех подрядчиков
# Создаем множества
contactor_1 = {"Кирпич", "Цемент", "Песок", "Арматура"}
contactor_2 = {"Цемент", "Бетон", "Арматура", "Гипс"}
contactor_3 = {"Утеплитель", "Керамзит", "Стекло", "Цемент"}
# Все уникальные
all_materials = contactor_1 | contactor_2 | contactor_3
print(f'Все уникальные - {all_materials}')
# общее для всех
common_materials = contactor_1 & contactor_2 & contactor_3
print(f'общее для всех - {common_materials}')
# Уникальные для 1
only_1 = contactor_1-contactor_2-contactor_3
print(f'Уникальные у первого - {only_1}')
# Есть только в одном из множеств
unique_to_each = contactor_1^contactor_2^contactor_3
print(f'Есть только в одном из множеств - {unique_to_each}')
