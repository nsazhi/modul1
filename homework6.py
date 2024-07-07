# Работа со словарями
my_dict = {'Таня' : 1996, 'Миша' : 2000, 'Вова' : 1998}
print(my_dict)
print(my_dict['Таня'],',', my_dict.get('Апполинарий', 'Я не знаю такого имени.'))
my_dict.update({'Олег' : 1985, 'Оля' : 1990})
print(my_dict)
a = my_dict.pop('Оля')
print(a)
print(my_dict)
# Работа с множествами
my_set = {25, 'string', True, 'string', 2, 2, 5, 25, True}
print(my_set)
my_set.update({35, 'boom'})
my_set.discard(True)
print(my_set)