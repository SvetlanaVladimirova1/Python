def get_data():
        data = []
        name = input('Введите фамилию: ')
        data.append(name)
        name1 = input('Введите имя: ')
        data.append(name1)          
        tel = input('Введите номер телефона: ')      
        data.append(tel)
        dop = input('Введите описание: ')
        data.append(dop)
        return (data)