# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

N = int(input('Введите число N: '))

list =  []

for i in range (N):
    list.append(random.randint(100, 1500))
    print(list[i]/100, end= ', ')   
max = list[0]/100%1
min = list[0]/100%1
for i in range (N):
    if  list[i]/100%1 > max:
        max = list[i]/100%1
    if  list[i]/100%1 < min: 
        min = list[i]/100%1 
print()  
a = round((max-min),2)     
print(a)

