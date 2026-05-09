# Задание 6
filepath = "/content/Example_1.ifc"
model = ifcopenshell.open(filepath)
walls = model.by_type("IfcWall") # Получение всех стен из модели
first_wall = walls[0] # Получение первой стены из списка
print(f"Name стены {first_wall.Name},\nObjectType стены {first_wall.ObjectType}" )
first_wall.Name = "MODIFIED_" + first_wall.Name
psets_wall = ifcopenshell.util.element.get_psets(first_wall)

for pset_name, props in psets_wall.items(): # Получение названия набора свойств
    for prop_name, value in props.items(): # Получение пары свойство-значение
        if prop_name == "IsExternal":
          props[prop_name] = not value # изменение значения в словаре

new_filepath = "1.ifc"
model.write(new_filepath)
model_new = ifcopenshell.open(new_filepath)
walls_new = model.by_type("IfcWall")
first_wall_new = walls_new[0] # Получение первой стены из списка
print(f"Name стены {first_wall_new.Name}" )
new_psets = ifcopenshell.util.element.get_psets(first_wall_new)
print(new_psets)
