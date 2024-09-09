my_dict = {'Roman': 2004, 'Lera': 2003}
print(my_dict)
print(my_dict['Roman'])
my_dict['Pavel'] = 2000
print(my_dict['Pavel'])
my_dict.update({'Denis': 2001, 'Potap': 2005})
print(my_dict)
a = my_dict.pop('Potap')
print(a)
print(my_dict)
my_set = set_ = {1,2,'apple',2,False,'apple','orange',1,False}
print(my_set)
set_.add(12.3)
set_.add((1,2,3))
set_.discard(False)
print(my_set)
