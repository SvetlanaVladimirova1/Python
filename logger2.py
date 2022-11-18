from vnesenie_dannyh import get_data as gd
data = gd()
def logger():
    with open ('spravochnik1.txt', 'a', encoding = 'utf-8') as file:
        file.write (f'{data[0]}, {data[1]}, {data[2]}, {data[3]}\n')
        file.write(f'\n')
        file.close()
def logger1():      
    with open ('spravochnik2.txt', 'a', encoding = 'utf-8') as file:
        file.write (f' {data[0]}\n {data[1]}\n {data[2]}\n {data[3]}\n')
        file.write(f'\n')
        file.close()