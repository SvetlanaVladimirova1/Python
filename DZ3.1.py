# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random


N = int(input('Введите целое число: '))
list = []
sum = 0
for i in range (N):
    list.append(random.randint(-N,N))
    if i%2 != 0:
        sum = sum + list[i]        
        print(f'на нечетных позициях: {list[i]}')   
print(list)                   
print(f'ответ:  {sum}')   


