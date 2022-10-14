#5. Реализуйте алгоритм перемешивания списка.

import random
N = int(input('Введите число: '))
list = []
for i in range(N):
    list.append(random.randint(1,N))
print(list)
for i in range(N//2):
    t = list[i]
    list[i] = list[(N-1-i)]
    list[N-1-i] = t                                                                                       
print(list)