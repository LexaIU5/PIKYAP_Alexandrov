#5 ЗАДАНИЕ
def print_result(func):
    def wrapper(*args, **kwargs):#при добавлении декоратора сначала вызывается wrapper
        result = func(*args, **kwargs)#вызов функции после декоратора
        print(func.__name__)
        if type(result) == list:
            for item in result:
                print(item)
        elif type(result) == dict:
            for k, v in result.items():
                print(k, " = ", v)
        else:
            print(result)
        return result #возвращаем результат
    return wrapper
@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()
