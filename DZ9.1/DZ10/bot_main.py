import telebot
import vnesenie_dannyh11

tokenID = '5400425841:AAFfgN_tlDu4KjEBqjD3jlYYTZ2I5h9mZLc'
t = telebot.TeleBot(tokenID)
employee1 = []
@t.message_handler(commands=['start'])
   
def Show_Menu(message):
   t.send_message(message.chat.id,'Выберите действие.\n')   
   t.send_message(message.chat.id,'1. Сложение.\n2. Вычитание.\n3. Умножение.\n4. Деление.\n')
@t.message_handler(content_types=['text'])

def Controller(message):
   txt =  message.text
   
   if txt == '1':
      t.send_message(message.chat.id,'Введите первое число ')
      t.register_next_step_handler(message,Get_f_number)   

   if txt == '2':
      t.send_message(message.chat.id,'Введите первое число ')
      t.register_next_step_handler(message,Get_f_number1)    

   if txt == '3':
      t.send_message(message.chat.id,'Введите первое число ')
      t.register_next_step_handler(message,Get_f_number2)    

   if txt == '4':
      t.send_message(message.chat.id,'Введите первое число ')
      t.register_next_step_handler(message,Get_f_number3)          
      
def Get_f_number(message):
   sum = message.text
   global employee1
   employee1.append(sum)
   t.send_message(message.chat.id,'Введите второе число ')
   t.register_next_step_handler(message,Get_second_number)

def Get_second_number(message):
   sum = message.text
   global employee1
   employee1.append(sum)
   vnesenie_dannyh11.Sum_New_Entry('employees.csv',employee1)
   employee1 = []
   Show_Menu(message)
   t.register_next_step_handler(message,Controller)   

def Get_f_number1(message):
   sub = message.text
   global employee1
   employee1.append(sub)
   t.send_message(message.chat.id,'Введите второе число ')
   t.register_next_step_handler(message,Get_second_number1)

def Get_second_number1(message):
   sub = message.text
   global employee1
   employee1.append(sub)
   vnesenie_dannyh11.Sub_New_Entry('employees.csv',employee1)
   employee1 = []
   Show_Menu(message)
   t.register_next_step_handler(message,Controller)    

def Get_f_number2(message):
   mult = message.text
   global employee1
   employee1.append(mult)
   t.send_message(message.chat.id,'Введите второе число ')
   t.register_next_step_handler(message,Get_second_number2)

def Get_second_number2(message):
   mult = message.text
   global employee1
   employee1.append(mult)
   vnesenie_dannyh11.Mult_New_Entry('employees.csv',employee1)
   employee1 = []
   Show_Menu(message)
   t.register_next_step_handler(message,Controller)          

def Get_f_number3(message):
   div = message.text
   global employee1
   employee1.append(div)
   t.send_message(message.chat.id,'Введите второе число ')
   t.register_next_step_handler(message,Get_second_number3)

def Get_second_number3(message):
   div = message.text
   global employee1
   employee1.append(div)
   vnesenie_dannyh11.Div_New_Entry('employees.csv',employee1)
   employee1 = []
   Show_Menu(message)
   t.register_next_step_handler(message,Controller)          

t.polling(non_stop=True)         