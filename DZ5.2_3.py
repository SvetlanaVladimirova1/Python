
#  b) Подумайте как наделить бота "интеллектом"

n = 2021
bot = n%(28+1)
print('Начало игры!')
print(f'Ход бота: {bot}')
n=n-bot
while n>0:
    first = int (input('Ваш ход, возьмите не более 28 конфет. Вы взяли сколько: '))
    print(first)
    if first >28 or first<=0:
        print('Недопустимый ход')
    elif   first>n:
        print(f'Столько нельзя, осталось всего {n}')  
    else:    
        n=n-first
        print(f'осталось {n}')
        if n==0:
            f = int (input('Вы выиграли! Конец игры. '))
            print(f)
        bot = 28+1-first
        print(f'Ход бота: {bot}')
        n=n-bot
        print(f'осталось {n} конфет')
else:
    f = int (input('Бот выиграл! Конец игры. '))
    print(f)