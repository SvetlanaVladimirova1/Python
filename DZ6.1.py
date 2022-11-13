# 3. Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму
#Пример:Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}
# Сумма 9.06
N = int(input('Введите число: '))
lst =[i for i in range(1,N+1)]
print(lst)
lst1 = list(map(lambda i: (round((1+1/i)**i,2)), lst))
print(lst1)
print(list(zip(lst, lst1)))
print(sum(lst1))
