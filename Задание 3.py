# Задание 3
filepath = "/content/Example_1.ifc"  
model = ifcopenshell.open(filepath)
walls = model.by_type("IfcWall") # Получение всех стен из модели
first_wall = walls[0] # Получение первой стены из списка
psets = ifcopenshell.util.element.get_psets(first_wall)
print("Полный словарь Property Sets:")
print(psets)
for pset_name, props in psets.items(): # Получение названия набора свойств
    print(f"Pset: {pset_name}")
    for prop_name, value in props.items(): # Получение пары свойство-значение
        print(f"  {prop_name}: {value}")
