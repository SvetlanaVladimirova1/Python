#Создайте программу для игры в "Крестики-нолики".

txt = '11 12 13'
list = txt.split( )
print(list)
txt1 = '21 22 23'
list1 = txt1.split( )
print(list1)
txt2 = '31 32 33'
list2 = txt2.split( )
print(list2)
while True:
    if list[0] == list[1] and list[1] == list[2] or list1[0] == list1[1] and list1[1] == list1[2] or\
        list2[0] == list2[1] and list2[1] == list2[2] or list[0] == list1[0] and list1[0] == list2[0] or\
        list[1] == list1[1] and list1[1] == list2[1] or list[2] == list1[2] and list1[2] == list2[2] or\
        list[0] == list1[1] and list1[1] == list2[2] or list[2] == list1[1] and list1[1] == list2[0]:  
        a = input('Вы выиграли! Конец игры. ')
        print(a)
    else:
        f = input('Первый игрок, выберите свободную координату. При неверной координате Вы пропускаете ход: ')
        first = input('Нажмите x и ENTER: ')
        print(first) 
        if f==list[0]:
            list[0] = first 
        if f==list[1]:
            list[1] = first
        if f==list[2]:
            list[2] = first
        if f==list1[0]:
            list1[0] = first
        if f==list1[1]:
            list1[1] = first
        if f==list1[2]:
            list1[2] = first     
        if f==list2[0]:
            list2[0] = first
        if f==list2[1]:
            list2[1] = first
        if f==list2[2]:
            list2[2] = first 
        print(list)
        print(list1)
        print(list2)   
    if list[0] == list[1] and list[1] == list[2] or list1[0] == list1[1] and list1[1] == list1[2] or\
        list2[0] == list2[1] and list2[1] == list2[2] or list[0] == list1[0] and list1[0] == list2[0] or\
        list[1] == list1[1] and list1[1] == list2[1] or list[2] == list1[2] and list1[2] == list2[2] or\
        list[0] == list1[1] and list1[1] == list2[2] or list[2] == list1[1] and list1[1] == list2[0]: 
        a = input('Вы выиграли! Конец игры. ')
        print(a)
    else:
        s = input('Второй игрок, выберите свободную координату. При неверной координате Вы пропускаете ход:  ')
        second = input('Нажмите o и ENTER: ')
        print(second) 
        if s==list[0]:
            list[0] = second
        if s==list[1]:
            list[1] = second
        if s==list[2]:
            list[2] = second
        if s==list1[0]:
            list1[0] = second
        if s==list1[1]:
            list1[1] = second
        if s==list1[2]:
            list1[2] = second   
        if s==list2[0]:
            list2[0] = second
        if s==list2[1]:
            list2[1] = second
        if s==list2[2]:
            list2[2] = second 
        
    print(list)
    print(list1)
    print(list2)  
 