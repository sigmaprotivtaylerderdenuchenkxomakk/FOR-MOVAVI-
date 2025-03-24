from telebot import *
from user import *
from kb import *
TOKEN = "7945274007:AAG2M3Fx6JGFFrvs73Pied_mfiQiU3Fp_3I"



bot = TeleBot(TOKEN)

#create_mov_db()



@bot.message_handler(commands=['start'])
def handle_start(message):
        bot.send_message(message.chat.id,('Здравствуйте, вас приветствует чат-бот для онбординга новых сотрудников в школу Movavi' ))
        bot.send_message(message.chat.id,'Пожалуйста, выберите свою роль', reply_markup = main_kb)
        
@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    if callback.data == 'teacher':
        User.save_user(callback.message.from_user.id,callback.data)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id,'Выбирите что хотите узнать', reply_markup = tutor_kb)

    elif callback.data == 'tutor':
        User.save_user(callback.message.from_user.id,callback.data)
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
        bot.send_message(callback.message.chat.id,'Выбирите что хотите узнать', reply_markup = teacher_kb)
    elif callback.data == 'axo':
         bot.send_message(callback.message.chat.id, 'Если вас интерисуют организиционые хозяйственные вопросы', reply_markup = tutor_kb_axo)
    elif callback.data == 'motivation':
         bot.send_message(callback.message.chat.id, 'Про мотивыцию', reply_markup = tutor_kb_motivation)
    elif callback.data == 'inst_reg':
         bot.send_message(callback.message.chat.id, 'Инструкции и регламенты', reply_markup = tutor_kb_inst_reg)
    elif callback.data == 'cpm':
         bot.send_message(callback.message.chat.id, 'CPM', reply_markup = tutor_kb_cpm)
    elif callback.data == 'mapcourses':
         bot.send_message(callback.message.chat.id, 'Карта курсов', reply_markup = tutor_kb_map_courses)
    elif callback.data == 'partners':
         bot.send_message(callback.message.chat.id, 'Партнеры', reply_markup = tutor_kb_partners)
    elif callback.data == 'growth':
         bot.send_message(callback.message.chat.id, 'Наши стратегии развития', reply_markup = tutor_kb_growth)
    elif callback.data == 'proschool':
         bot.send_message(callback.message.chat.id, 'Проскул', reply_markup = tutor_kb_pro_school)
    elif callback.data == '10gym':
         bot.send_message(callback.message.chat.id, '10-ая гимназия', reply_markup = tutor_kb_10th_gymnasium)
    
    


bot.polling(non_stop=True, interval=1)  

