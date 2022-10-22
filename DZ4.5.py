# Даны два файла, в каждом из которых находится запись многочлена. 
#Задача - сформировать файл, содержащий сумму многочленов.

f = open('file1.txt','r')  
for i in f:
    print(i, end='')
    import re
n = re.findall('\d+', i)
print(n)
f.close()
f1 = open('file1.1.txt','r')  
for e in f1:
    print(e, end='')
    print()
    m = re.findall('\d+', e)
    print(m)
f1.close()
f2 = open('file3.txt','w')  
f2.write(str(int(n[0])+int(m[0]))+'*x**2+'+(str(int(n[2])+int(m[2])))+'*x+'+(str(int(n[3])+int(m[3])))+'=0')
f2.close()

