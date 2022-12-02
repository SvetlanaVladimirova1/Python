from datetime import datetime

def Sum_New_Entry(f,list):
    a = float(list[0])
    b = float(list[1])
    sum = a + b
    time=datetime.now().strftime('%D %H:%M')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f' {time}    {a} + {b} = {sum};\n')

def Sub_New_Entry(f,list):
    a = float(list[0])
    b = float(list[1])
    x = a - b
    time=datetime.now().strftime('%D %H:%M')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f' {time}    {a} - {b} = {x};\n')  

def Mult_New_Entry(f,list):
    a = float(list[0])
    b = float(list[1])
    x = a * b
    time=datetime.now().strftime('%D %H:%M')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f' {time}    {a} * {b} = {x};\n')  

def Div_New_Entry(f,list):
    a = float(list[0])
    b = float(list[1])
    x = round (a / b, 3)
    time=datetime.now().strftime('%D %H:%M')
    with open('employees.csv','a', encoding='utf-8') as book:
        book.write(f' {time}    {a} / {b} = {x};\n') 