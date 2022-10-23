# Задача 5 НЕОБЯЗАТЕЛЬНАЯ. Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z .
# Но теперь количество предикатов не три, а генерируется случайным образом от 5 до 25, сами значения предикатов случайные,
# проверяем это утверждение 100 раз, с помощью модуля time выводим на экран , сколько времени отработала программа.

import random
import time

startTime = time.time()
for i in range(100):
    n = random.randint(5, 25)
    print(f'Количество предикатов = {n}')

    predicats = []
    pred = [True, False]

    for j in range(n):
        predicats.append(random.choice(pred))
    print(predicats)

    left = True
    right = True
    for i in range(n):
        if predicats[i] == True:
            left = not True
        elif not predicats[i] == False:
            right = False

    print(left == right)
    print()

print(f'Программа отработала {time.time()-startTime} секунд')
