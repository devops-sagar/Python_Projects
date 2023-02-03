# def my_func(x, y=[]):
#     y.append(x)
#     return y

# print(my_func(1))
# print(my_func(2))
# print(my_func(3))

# li = [10]
# print(sum(li, 30))

import pyautogui as pg
import random
import time

while True:
    x = random.randint(600, 700)
    y = random.randint(200, 600)
    pg.moveTo(x, y, 2)
    time.sleep(2)