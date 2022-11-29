def print_all_to_console():
    list = []
    with open('employees.csv', encoding="utf-8") as data:
        for line in data:
            list.append(line.replace(',', ' '))

    return list