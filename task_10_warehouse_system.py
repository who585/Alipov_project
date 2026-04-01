# Система учета склада
# Исходные данные
warehouse = {
    "Кирпич": {"quantity": 5000, "price": 12.50, "min_quantity": 1000},
    "Цемент": {"quantity": 120, "price": 450.00, "min_quantity": 50},
    "Песок": {"quantity": 8, "price": 800.00, "min_quantity": 10},
    "Арматура": {"quantity": 30, "price": 48000.00, "min_quantity": 20},
    "Бетон": {"quantity": 45, "price": 4200.00, "min_quantity": 15}
}
# Шапка
print("="*50)
print("СИСТЕМА УЧЁТА СКЛАДА")
print("="*50)
print("Материал | Кол-во | Цена | Мин. | Стоимость")
print("="*50)
# задаем переменные для расчета
max_price= 0
all_cost = 0
crit=[]
for material, count in warehouse.items():
  # Расчет общей стоимости
  cost=count["quantity"]*count["price"]
  all_cost+=cost
  # Вывод склада и критич остатка
  if count["quantity"] > count["min_quantity"]:
    print(f"{material} | {count["quantity"]} | {count["price"]} | {count["min_quantity"]} | {count["quantity"]*count["price"]} ")
  else:
    crit.append((material, count["quantity"],count["min_quantity"])) # Собираем все критич остатки в одну переменную и записываем нужные параметры
    print(f"{material} | {count["quantity"]} | {count["price"]} | {count["min_quantity"]} | {count["quantity"]*count["price"]} !!! КРИТИЧ !!!")
  # Вывод самого дорого материала
  if cost > max_price:
    max_price = cost
    max_material=material
# Вывод значений
print("="*50)
print(f"Общая стоимость {all_cost}")   
print(f"Самый дорогой:{max_material}({max_price})")
print(f"!!! Критические остатки: {len(crit)}")
for material, quantity, min_qty in crit: # Проходимя по всем параметрам критич остатка, которые записали ранее
        print(f"- {material}: {quantity} < {min_qty}")
# Моделирование выдачи
print("=== ВЫДАЧА МАТЕРИАЛА ===")
material = "Цемент"
count = 25
new_count=warehouse[material]["quantity"]-count
print(f"Выдано {count} единиц {material}")
print(f"Остаток: {warehouse[material]["quantity"]} -> {new_count}")
