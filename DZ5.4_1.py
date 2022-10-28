# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример
# 	а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E

list = []
txt = 'A A A A A A F D D C C C C C C C A E E E E E E E E E E E E E E E E E'
a = txt.split()
print(a)
current = a[0]
counter = 0
for i in a:
    if i == current:
        counter += 1       
    else:
        list.append((counter, current))
        current = i
        counter = 1
list.append((counter, current))                                             
print(list)                                       


