from telebot import *
from user import *
from kb import *
from config import *
import db_create 
db_create.create_db()
bot = TeleBot(TOKEN)

# create_mov_db()


@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(
        message.chat.id, ('Здравствуйте, вас приветствует чат-бот для онбординга новых сотрудников в школу Movavi'))
    bot.send_message(
        message.chat.id, 'Пожалуйста, выберите свою роль', reply_markup=main_kb)
    


@bot.callback_query_handler(func=lambda callback: True)
def handle_callback(callback):
    user: str = User.get_user_by_id(callback.from_user.id)
    if callback.data == 'teacher' and user == 'Пользователь не найден':
        User.save_user(callback.from_user.id, callback.data)
        bot.edit_message_text(text='Выбирите что хотите узнать',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=teacher_kb, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'tutor' and user == 'Пользователь не найден':
        User.save_user(callback.from_user.id, callback.data)
        bot.edit_message_text(text='Выбирите что хотите узнать',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'tutor' and user == 'tutor':
        bot.edit_message_text(text='Выбирите что хотите узнать',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == ' tutor' and user == 'teacher':
        bot.edit_message_text(text='Выбирите что хотите узнать',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=teacher_kb, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'teacher' and user == 'teacher':
        bot.edit_message_text(text='Выбирите что хотите узнать',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=teacher_kb, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'teacher' and user == 'tutor':
        bot.edit_message_text(text='Выбирите что хотите узнать',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'axo':
        bot.edit_message_text(text='Если вас интересуют организиционые хозяйственные вопросы',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb_axo, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'motivation':
        bot.edit_message_text(text='Про мотивацию',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb_motivation, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'inst_reg':
        bot.edit_message_text(text='Инструкции и регламенты',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb_inst_reg, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'cpm':
        bot.edit_message_text(
            text='CPM', chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb_cpm, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'mapcourses':
        bot.edit_message_text(
            text='Карта курсов', chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(reply_markup=tutor_kb_map_courses,
                                      chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'partners':
        bot.edit_message_text(
            text='Партнеры', chat_id=callback.message.chat.id, message_id=callback.message.id)
        bot.edit_message_reply_markup(
            reply_markup=tutor_kb_partners, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'growth':
        bot.edit_message_text(text='Наши стратегии развития',
                              chat_id=callback.message.chat.id, message_id=callback.message.id)
        rol: str = User.get_user_by_id(callback.from_user.id)
        if rol == "tutor":
            bot.edit_message_reply_markup(
                reply_markup=tutor_kb_growth, chat_id=callback.message.chat.id, message_id=callback.message.id)
        else:
            bot.edit_message_reply_markup(
                reply_markup=teacher_kb_growth, chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == 'proschool':
        rol: str = User.get_user_by_id(callback.from_user.id)
        bot.edit_message_text(
            text='Проскул', chat_id=callback.message.chat.id, message_id=callback.message.id)
        if rol == "tutor":
            bot.edit_message_reply_markup(
                reply_markup=tutor_kb_pro_school, chat_id=callback.message.chat.id, message_id=callback.message.id)
        else:
            bot.edit_message_reply_markup(reply_markup=teacher_kb_pro_school,
                                          chat_id=callback.message.chat.id, message_id=callback.message.id)
    elif callback.data == '10gym':
        rol: str = User.get_user_by_id(callback.from_user.id)

        bot.edit_message_text(
            text='10-ая гимназия', chat_id=callback.message.chat.id, message_id=callback.message.id)
        if rol == "tutor":
            bot.edit_message_reply_markup(reply_markup=tutor_kb_10th_gymnasium,
                                          chat_id=callback.message.chat.id, message_id=callback.message.id)
        else:
            bot.edit_message_reply_markup(reply_markup=teacher_kb_10th_gymnasium,
                                          chat_id=callback.message.chat.id, message_id=callback.message.id)


bot.polling(non_stop=True, interval=1)
