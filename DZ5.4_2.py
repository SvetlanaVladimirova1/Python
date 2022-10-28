# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример а) AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE => 6A1F2D7C1A17E
            
list = []
txt = '6 A 1 F 2 D 7 C 1 A 17 E'
a = txt.split()
print(a)
counter = ' '
for i in range(len(a)):
    if a[i].isdigit():
        counter = counter + a[i]
    else: 
        list.append((int(counter)*a[i]))
        counter = ' '
print(list)    
                                   