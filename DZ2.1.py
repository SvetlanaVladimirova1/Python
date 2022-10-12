# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

#  Пример:
# 6782 -> 23
# 0,56 -> 11

N = float(input('Введите число N: '))
print(N)
S = str(N)
sum = 0
for i in range(len(S)):
    if (S[i]) == ".":
        i = i+1
    else:    
        print(S[i])
        sum = sum + int(S[i])
    
print(sum, end= " Сумма") 
