import search1
import print
import telebot
import vnesenie_dannyh

tokenID = 'токен'
t = telebot.TeleBot(tokenID)
employee1 = []
@t.message_handler(commands=['start'])
   
def Show_Menu(message):
   t.send_message(message.chat.id,'1. Вывести все записи телефонной книги.\n2. Добавить запись.\n3. Найти запись.\n')
@t.message_handler(content_types=['text'])

def Controller(message):
   txt =  message.text
   if txt == '1':
         empl_list = print.print_all_to_console()
         for i in empl_list:
             t.send_message(message.chat.id, i)
   if txt == '2':
      t.send_message(message.chat.id,'Введите фамилию')
      t.register_next_step_handler(message,Get_Sirname)   
   
   if txt == '3':
      t.send_message(message.chat.id,'Введите фамилию для поиска в БД')
      t.register_next_step_handler(message,Search)  
      
def Get_Sirname(message):
   sirname = message.text
   global employee1
   employee1.append(sirname)
   t.send_message(message.chat.id,'Введите имя')
   t.register_next_step_handler(message,Get_Name)
   
def Get_Name(message):
   name = message.text
   global employee1
   employee1.append(name)
   t.send_message(message.chat.id,'Введите номер телефона')
   t.register_next_step_handler(message,Get_Phone)  

def Get_Phone(message):
   phone = message.text
   global employee1
   employee1.append(phone)
   t.send_message(message.chat.id,'Введите дополнительную информацию')
   t.register_next_step_handler(message,Get_Dop)

def Get_Dop(message):
   dop = message.text
   global employee1
   employee1.append(dop)
   vnesenie_dannyh.New_Entry('employees.csv',employee1)
   employee1 = []
   Show_Menu(message)
   t.register_next_step_handler(message,Controller)       

def Search(message):
   name1   = message.text
   empl_list1 = search1.Search_Entry()
   for e in empl_list1:
             if name1 in e:
               t.send_message(message.chat.id, e)
   Show_Menu(message)
   t.register_next_step_handler(message,Controller)         
             
t.polling(non_stop=True)      


