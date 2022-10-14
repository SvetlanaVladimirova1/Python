# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.



import random
N = int(input('Введите число: '))
list = []
for i in range(N):
    list.append(random.randint(-N,N))
print(list)
f = open('file.txt','r')
num = f.readlines()
print(num)   
f.close()  