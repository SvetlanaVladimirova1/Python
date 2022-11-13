# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
n=8
def fib(x):
    if x in [1, 2]:
        return 1
    elif x in [0]:
        return 0
    else:
        return fib(x-1) + fib(x-2)
list = [fib(i) for i in range (1,n+1)]
list1 = [fib(i)*(-1)**(i+1) for i in range (n+1)]
print(list1[::-1]+list)