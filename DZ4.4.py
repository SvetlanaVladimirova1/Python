# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
#(значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
k = 3
list = []
for i in range ((k+1)):
    list.append(random.randint(0,100))
print(list)  
for i in range ((k+1)):
    print(f'{list[i]}*x^{k}+{list[(i+1)]}*X^{(k-1)}+{list[(i+2)]}*x^{(k-2)}+{list[(i+3)]}=0') 

    f = open('file2.txt','a') 
    f.write(str(list[i])+'*x^'+str(k)+'+'+str(list[(i+1)])+'*X^'+str((k-1))+'+'+str(list[(i+2)])+'*x^'+str((k-2))+'+'+str(list[(i+3)])+'=0')
    f.write('\n')
    f.close()
