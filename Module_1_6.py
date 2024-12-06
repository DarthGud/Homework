my_dict= {'Andrey': 2001, 'Misha': 2003}
print (my_dict.get('Andrey', 'Ключ отсутствует'), my_dict.get('Masha', 'Ключ отсутствует'))
my_dict.update({'Masha': 1999, 'Vova': 2004})
print(my_dict)
print (my_dict.pop('Masha'))
print(my_dict)

my_set = {1, 'Russia',3.75, 'Russia', 1}
print (my_set)
my_set.update({'China', 10})
my_set.discard(1)
print (my_set)