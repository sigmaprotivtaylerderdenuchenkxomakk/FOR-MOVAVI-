from telebot import *

from kb import *
TOKEN = "7945274007:AAG2M3Fx6JGFFrvs73Pied_mfiQiU3Fp_3I"



bot = TeleBot(TOKEN)

#create_mov_db()



@bot.message_handler(commands=['start'])
def handle_start(message):
        bot.send_message(message.chat.id,('Здравствуйте, вас приветствует чат-бот для онбординга новых сотрудников в школу Movavi' ))
        
        bot.send_message(message.chat.id,'Пожалуйста, выберите свою роль',
reply_markup = main_kb)
        


          

bot.polling(non_stop=True, interval=1)  

