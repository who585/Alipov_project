import ifcopenshell
import ifcopenshell.util.element
# Задание 1
filepath = "/content/Example_1.ifc"  
model = ifcopenshell.open(filepath)
walls = model.by_type("IfcWall") # Получение всех стен из модели
print(f"Количество стен в модели {len(walls)}")
