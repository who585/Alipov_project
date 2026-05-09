# Задание 2
filepath = "/content/Example_1.ifc"  
model = ifcopenshell.open(filepath)
walls = model.by_type("IfcWall") # Получение всех стен из модели
print(f"Количество стен в модели {len(walls)}")
first = walls[0] # Получение первой стены из списка
print(f"GlobalId стены {first.GlobalId},\nName стены {first.Name},\nObjectType стены {first.ObjectType}" )
