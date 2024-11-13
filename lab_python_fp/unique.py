#3 ЗАДАНИЕ
# Нужно реализовать конструктор
# В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
# в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
# Например: ignore_case = True, Aбв и АБВ - разные строки
#           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
# По-умолчанию ignore_case = False
# Итератор для удаления дубликатов
class Unique(object):
    def __init__(self, items, **kwargs):
        self.items = items
        self.ignore = kwargs.get("ignore_case", False)
        self.Set = set() #для уникальных значений
    def __next__(self):
       for item in self.items:
           to_low = item.lower() if self.ignore and type(item) == str else item
           if to_low not in self.Set:
               self.Set.add(to_low)
               return item
       raise StopIteration #для генерации исключений
    def __iter__(self):
        return self
    
data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
unique_data1 = Unique(data1)
print(list(unique_data1))

data2 = (x for x in gen_random(10, 1, 3)) 
unique_data2 = Unique(data2)
print(list(unique_data2))

data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
unique_data3 = Unique(data3)
print(list(unique_data3))

unique_data4 = Unique(data3, ignore_case=True)
print(list(unique_data4))
