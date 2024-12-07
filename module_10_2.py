import threading
import time


class Knight(threading.Thread):

    def __init__(self, name, power):
        self.name_of_kn = name
        self.power = power
        super().__init__()

    def run(self):
        print(f'{self.name_of_kn}, на нас напали!')
        enemies = 100
        days = 0
        while enemies > 0:
            time.sleep(1)
            days += 1
            enemies -= self.power
            print(f'{self.name_of_kn}, сражается {days} дней(дня)..., осталось {enemies} воинов.')
        print(f'{self.name_of_kn} одержал победу спустя {days} дней(дня)!')


# Создание класса
first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
# Запуск потоков и остановка текущего
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
# Вывод строки об окончании сражения
print('Все битвы закончены!')
