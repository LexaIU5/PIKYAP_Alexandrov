#7 ЗАДАНИЕ
import json
import sys


path = r"D:\Users\79169\Загрузки\data_light.json"

with open(path, 'r', encoding='utf-8') as f:
    data = json.load(f)

@print_result
def f1(arg):
    return sorted(Unique(field(arg, 'job-name')))

@print_result
def f2(arg):
    return list(filter(lambda x: True if x.lower().startswith('программист') else False, arg))


@print_result
def f3(arg):
    return list(map(lambda x: x + ' с опытом Python', arg))


@print_result
def f4(arg):
    salary = gen_random(len(arg), 100000, 200000)
    return [i + ', зарплата {} руб.'.format(j) for i, j in zip(arg, salary)]
    

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
