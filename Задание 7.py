# Задание 7
filepath = "/content/Example_1.ifc"
model = ifcopenshell.open(filepath)
doors = model.by_type("IfcDoor")
min_width = 900 # Минимальная ширина

doors_to_remove = [d for d in doors
                   if getattr(d, "OverallWidth", 0) < min_width]

# Удаляем "узкие" двери 
for door in doors_to_remove:
    model.remove(door)

output_filename = "_doors_.ifc"
model.write(output_filename)

new_model = ifcopenshell.open(output_filename)
remaining_doors = new_model.by_type("IfcDoor")
print(f"В созданном файле {output_filename} дверей: {len(remaining_doors)}")
for door in remaining_doors:
    Width = getattr(door, "OverallWidth", None)
    print(f"  {door.Name}: ширина = {round(Width, 3)} мм")
