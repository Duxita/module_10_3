import threading
import random

import time
from threading import Thread, Lock
class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposite(self):
        for i in range(100):
            tranz = random.randint(50,500)
            self.balance += tranz
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f'Пополнение: {tranz}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for j in range(100):
            tranz_1 = random.randint(50,500)
            print(f'Запрос на снятие: {tranz_1}')
            if tranz_1 <= self.balance:
                self.balance -= tranz_1
                print(f'Снятие: {tranz_1}. Баланс: {self.balance}')
            else:
                print("Запрос отклонён, недостаточно средств!")
                self.lock.acquire()
bk = Bank()
th1 = threading.Thread(target=Bank.deposite, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
