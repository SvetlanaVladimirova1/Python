def Search_Entry():
    list = []
    with open('employees.csv', 'r', encoding="utf-8") as data:
                    for line in data:
                        list.append(line.replace(',', ' '))
    return list  
                            