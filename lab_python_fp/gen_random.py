#2 ЗАДАНИЕ
# gen_random(5, 1, 3) должен выдать выдать 5 случайных чисел
# в диапазоне от 1 до 3, например 2, 2, 3, 2, 1
def gen_random(num_count, begin, end):
    import random
    for i in range(num_count):
        yield random.randint(begin, end)
for num in gen_random(5, 1, 3):
    print(num)
