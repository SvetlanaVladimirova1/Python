# 3. Задайте список из n чисел последовательности (1+1/n)n и выведите на экран их сумму

#  Пример:

# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} 
# Сумма 9.06

N = int(input('Введите число: '))
for i in range (1,N+1):
    print(i)
for i in range(1,N+1):
    list= round((1+1/i)**i,2)
    print(list)
sum = 0
for i in range(1,N+1):
    sum = sum + round((1+1/i)**i,2)
print(sum, end= ' сумма    ')
d={i: round((1+1/i)**i,2) for i in range(1,N+1)}
print(d)

