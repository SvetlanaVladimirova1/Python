def print_element_to_console():
    print(f'Нажмите Enter')
    name = input()
    lines = []
    with open('employees.csv', 'r', encoding="utf-8") as data:
        for line in data:
                if not name in line: 
                    lines += line
                else:
                    lines = line.split(", ")
                    old = int(input("Номер элемента для вывода: 1 - ID; 2 - фамилия; 3 - имя; 4 - отчество; 5 - телефон; 6 - отдел; 7 - должность: "))
                    print(lines[old-1] )
                    lines = ", ".join(line)
                    lines += line              
