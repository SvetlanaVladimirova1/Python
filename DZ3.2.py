# Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random


N = int(input('Введите целое число: '))
list = []
for i in range (N):
    list.append(random.randint(1,N))
print(list)   

for i in range(N//2):   
    if N%2 == 0: 
        list[i] = list [i] * list[(N-1-i)]                                                                                          
        print(list[i], end= ', ')
for i in range(N//2+1):          
    if N%2 != 0:
        list[i] = list [i] * list[(N-1-i)]                                                                                          
        print(list[i], end= ', ')



