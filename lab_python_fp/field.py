#1 ЗАДАНИЕ
goods = [
   {'title': 'Ковер', 'price': 2000, 'color': 'green'},
   {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}
]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0 # проверка на истинность, иначе AssertionError
    
    if len(args) == 1:
        for i in items:
            result = i[args[0]]
            if result != None:
                yield result
    else:
        for item in items:
            result = {i:item[i] for i in args if item[i] != None} #создаем словарь, если значение не None
            yield result
    
print(*list(field(goods, 'title', 'price')))
