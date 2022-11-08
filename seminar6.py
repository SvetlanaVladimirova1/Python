# import math
# n = int(input('Введите количество цифр после запятой: '))
# print('Число 𝜋: {:.50f}'.format(math.pi))
# a = math.pi
# b = round(a,n+1)*10**n
# c = math.modf(b)
# a = c[1] / 10**n
# print(f'Число 𝜋 с заданной точностью:  {a:.50f}  ')






formula = '24/2*3+30'
lst = []
numbers = ''

def Action(array,sign):
    i = 0
    while sign in array:
        if array[i] == sign:
            if sign == '*':
                a = int(array[i-1])*int(array[i+1])
            elif sign == '/':
                a = int(array[i-1])/int(array[i+1])
            elif sign == '-':
                a = int(array[i-1])-int(array[i+1])
            elif sign == '+':
                a = int(array[i-1])+int(array[i+1])
            array[i-1] = a
            array.pop(i+1)
            array.pop(i)
            return(array)
        else:
            i+=1
for i in formula:
    if i.isdigit():
        numbers+=i
    else:
        lst.append(numbers)
        numbers=''
        lst.append(i)
lst.append(numbers)
print(lst)

i = 0
while '/' in lst or '*' in lst:
    if lst[i] == '/':
        print(Action(lst,'/'))
        i = 0
    elif lst[i] == '*':
        print(Action(lst,'*'))
        i = 0
    else:
        i+=1

i = 0
while '-' in lst or '+' in lst:
    if lst[i] == '-':
        print(Action(lst,'-'))
        i = 0
    elif lst[i] == '+':
        print(Action(lst,'+'))
        i = 0
    else:
        i+=1
print(lst)
