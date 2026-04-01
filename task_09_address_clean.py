# Очистка адресов
# Исходные данные
addresses = [ 
"  г. Москва, ул. Ленина, д. 10  ", 
"г.Казань,ул.Баумана,д.15", 
"  г. Санкт-Петербург, ул. Невский, д. 100  " 
]
# Создаем пустой список
cleaned_addresses = []
# Прогоняем каждый адрес
for address in addresses:
  address_1=address.strip().replace(" ","").replace(".",". ").replace(",",", ")
  cleaned_addresses.append(address_1) # Добавляем в пустой список адреса
print(f'#1\nДо: {addresses[0]} \nПосле: {cleaned_addresses[0]}')
print(f'#2\nДо: {addresses[1]} \nПосле: {cleaned_addresses[1]}')
print(f'#3\nДо: {addresses[2]} \nПосле: {cleaned_addresses[2]}')
