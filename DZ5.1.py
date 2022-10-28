#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
list1=[]
txt = 'абв асб ннн аб абвг абве абв абв абв'
list = txt.split( )
print(list)
for i in range(len(list)):   
        if "абв" in list[i]:
            print(list[i])
            list[i] = ' '            
for i in range(len(list)):
        if list[i] != ' ':
            list1.append(list[i])                        
print(list1)