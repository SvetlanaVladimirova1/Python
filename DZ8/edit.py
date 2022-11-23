def Edit_Entry(file):

    print(f'Введите элемент данных сотрудника для изменения данных о нём в БД: ')
    name = input()
    lines = []
    
    with open(file, 'r', encoding="utf-8") as data:
            for line in data:
                if not name in line: 
                    lines += line
                else:
                    line = line.split(", ")
                    print(line)
                    old = int(input("Номер элемента для замены от 1 до 7: "))
                    new = input("На что заменить: ")
                    line[old-1] = new
                    line = ", ".join(line)
                    lines += line

    with open(file, 'w', encoding="utf-8") as data:
            data.writelines(lines)
        
    print('Изменение произведено...')