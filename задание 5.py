# Задание 5
filepath = "/content/Example_1.ifc"  
model = ifcopenshell.open(filepath)
doors = model.by_type("IfcDoor")
min_width = 900 # Минимальная ширина
malenkie_doors = []
for door in doors:
    name = getattr(door, "Name", None)
    width = getattr(door, "OverallWidth", None)
    height = getattr(door, "OverallHeight", None)
    if width < min_width:
        malenkie_doors.append((name, width, height)) # Добавление маленьких дверей в список
        print(f"{name}: ширина = {round(width,3)}, высота = {round(height,3)}") 
if len(malenkie_doors) == 0:
  print('Маленьких нету')
else:
  print(f'Количество маленьких дверей: {len(malenkie_doors)}')
     
