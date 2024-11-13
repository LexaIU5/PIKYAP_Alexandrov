#6 ЗАДАНИЕ
#1 cm_timer_1 на примере класса
import time
from contextlib import contextmanager
class cm_timer_1:
    def __enter__(self): #дейтсвия до основного кода
        self.start_time = time.time() #сохраняем время начала
        return self
    def __exit__(self, exc_type, exc_value, traceback): #после выполнения with
        #exc_type - исключение внутри with
        #exc_value - сообщение об ошибке
        #traceback показывает, где произошла ошибка
        print(time.time() - self.start_time, "- время выполнения cm_timer_1")
if __name__ == "__main__":
    with cm_timer_1():
        time.sleep(5.5)

@contextmanager
def cm_timer_2():
    start_time = time.time()
    try:
        yield #до кода выполняется, после передает управление with
    finally: #после with возвращаемся в finally
        print(time.time() - start_time, "- время выполнения cm_timer_2")
if __name__ == "__main__":
    with cm_timer_2():
        time.sleep(5.5)
