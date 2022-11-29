def New_Entry(f,list):
    sirname = list[0]
    name = list[1]
    phone = list[2]
    dop = list[3]
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f'{sirname}, {name}, {phone}, {dop};\n')
        