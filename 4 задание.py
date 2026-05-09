# Задание 4
filepath = "/content/Example_1.ifc"  
model = ifcopenshell.open(filepath)
storeys = model.by_type("IfcBuildingStorey")
print(f"Схема IFC: {model.schema}")
print(f"Количество этажей: {len(storeys)}")
for storey in storeys:
    if storey.Elevation == None:
      storey.Elevation = None # Замена пустоты на None
    print(f"Этаж: {storey.Name}, Elevation={storey.Elevation}")
