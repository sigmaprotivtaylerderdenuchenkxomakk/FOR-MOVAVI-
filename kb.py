from telebot import *


TOKEN = "7945274007:AAG2M3Fx6JGFFrvs73Pied_mfiQiU3Fp_3I"

bot = TeleBot(TOKEN)



main_kb = types.InlineKeyboardMarkup(
    row_width = 1
)

button_tutor = types.InlineKeyboardButton(
    text = 'Я куратор', callback_data = 'tutor')

button_teacher = types.InlineKeyboardButton(
  text = 'Я преподаватель', callback_data = 'teacher')

main_kb.add(button_tutor,button_teacher)


#Главные кнопки (куратор)

tutor_kb = types.InlineKeyboardMarkup(
    row_width = 1
)

button_link_about_company = telebot.types.InlineKeyboardButton(
    'О компании', url='https://robotmovavi.ru/')

button_inst_reg = types.InlineKeyboardButton(
    text = 'Инструкция и регламенты', callback_data = 'inst_reg')

button_map_courses = types.InlineKeyboardButton(
    text = 'Карта курсов', callback_data = 'mapcourses')


button_what_where_why = types.InlineKeyboardButton(
    'Стрктура Кто? Где? Когда?', url='https://robotmovavi.ru/')

button_partners = types.InlineKeyboardButton(
    text = 'Партнеры', callback_data = 'partners')

button_motivation = types.InlineKeyboardButton(
    text = 'Мотивация', callback_data = 'motivation')

button_axo = types.InlineKeyboardButton(
    text = 'AXO', callback_data = 'axo')

button_back = types.InlineKeyboardButton(
    text = 'AXO', callback_data = 'back')

tutor_kb.add(button_link_about_company, button_inst_reg, button_map_courses, button_what_where_why, button_partners, button_motivation, button_axo, button_back)


#Инструкции и регламенты (куратор)

tutor_kb_inst_reg = types.InlineKeyboardMarkup(
    row_width = 1
)

button_link_documentory = telebot.types.InlineKeyboardButton(
    'Документоборот', url='https://robotmovavi.ru/')

button_link_cash_desk = telebot.types.InlineKeyboardButton(
    'Касса', url='https://robotmovavi.ru/')

button_link_fire_evacuation = telebot.types.InlineKeyboardButton(
    'Пожарная эвакуация', url='https://robotmovavi.ru/')

button_link_counterparties = telebot.types.InlineKeyboardButton(
    'Работа с контрагентами', url='https://robotmovavi.ru/')

button_link_first_aid = telebot.types.InlineKeyboardButton(
    'Первая помощь', url='https://robotmovavi.ru/')

button_cpm = telebot.types.InlineKeyboardButton(
    text = 'CPM', callback_data = 'cpm')


tutor_kb_inst_reg.add(button_link_documentory, button_link_cash_desk, button_link_fire_evacuation, button_link_counterparties, button_link_first_aid, button_cpm)


#Инструкции и регламенты --- CPM (куратор)

tutor_kb_cpm = types.InlineKeyboardMarkup(
    row_width = 1
)

button_create_contract = telebot.types.InlineKeyboardButton(
    'Как создать договор', url='https://robotmovavi.ru/')

button_pay = telebot.types.InlineKeyboardButton(
    'Как провести оплату', url='https://robotmovavi.ru/')




#Карта курсов (куратор)

tutor_kb_map_courses = types.InlineKeyboardMarkup(
    row_width = 1
)

button_summer_camp = telebot.types.InlineKeyboardButton(
    'Летняя школа', url='https://robotmovavi.ru/')

button_main_courses = telebot.types.InlineKeyboardButton(
    'Основные курсы', url='https://robotmovavi.ru/')

button_link_short_term_groups = telebot.types.InlineKeyboardButton(
    'Краткосрочные группы', url='https://robotmovavi.ru/')


tutor_kb_map_courses.add(button_summer_camp, button_main_courses, button_link_short_term_groups)




#Партнеры (куратор)

tutor_kb_partners = types.InlineKeyboardMarkup(
    row_width = 1
)

button_partners_growth = telebot.types.InlineKeyboardButton(
    text = 'Рост', callback_data = 'growth')

button_partners_pro_school = telebot.types.InlineKeyboardButton(
    text = 'Проскул', callback_data = 'proschool')

button_partners_10th_gymnasium = telebot.types.InlineKeyboardButton(
    text = '10-ая гимназия', callback_data = '10gym')


tutor_kb_partners.add(button_partners_growth, button_partners_pro_school, button_partners_10th_gymnasium)




#Партнеры --- Рост (куратор)

tutor_kb_growth = types.InlineKeyboardMarkup(
    row_width = 1
)

button_grouth_olympiad = telebot.types.InlineKeyboardButton(
    'Олимпиада', url='https://robotmovavi.ru/')

button_grouth_courses = telebot.types.InlineKeyboardButton(
    'Курсы', url='https://robotmovavi.ru/')


tutor_kb_growth.add(button_grouth_olympiad, button_grouth_courses)




#Партнеры --- Проскул (куратор)

tutor_kb_pro_school = types.InlineKeyboardMarkup(
    row_width = 1
)

button_pro_school_courses = telebot.types.InlineKeyboardButton(
    'Курсы', url='https://robotmovavi.ru/')


tutor_kb_pro_school.add(button_pro_school_courses)





#Партнеры --- 10ая гимназия (куратор)

tutor_kb_10th_gymnasium = types.InlineKeyboardMarkup(
    row_width = 1
)

button_10th_gymnasium_courses = telebot.types.InlineKeyboardButton(
    'Курсы', url='https://robotmovavi.ru/')


tutor_kb_10th_gymnasium.add(button_10th_gymnasium_courses)




#Мотивация (куратор)

tutor_kb_motivation= types.InlineKeyboardMarkup(
    row_width = 1
)

button_motivation_feedback = telebot.types.InlineKeyboardButton(
    'Обратная связь', url='https://robotmovavi.ru/')

button_motivation_mov_boost = telebot.types.InlineKeyboardButton(
    'Мовави Буст Инструкция/пароли', url='https://robotmovavi.ru/')


tutor_kb_motivation.add(button_motivation_feedback, button_motivation_mov_boost)





#AXO (куратор)

tutor_kb_axo= types.InlineKeyboardMarkup(
    row_width = 1
)

button_axo_useful_phonenum = telebot.types.InlineKeyboardButton(
    'Полезные телефоны', url='https://robotmovavi.ru/')



tutor_kb_axo.add(button_axo_useful_phonenum)







#Главные кнопки (преподаватель)

teacher_kb = types.InlineKeyboardMarkup(
    row_width = 1
)


button_t_partners = types.InlineKeyboardButton(
    text = 'Партнеры', callback_data = 'partnerst')


button_working_method = types.InlineKeyboardButton(
    'Метод работы', url='https://robotmovavi.ru/')


tutor_kb.add(button_link_about_company, button_what_where_why, button_map_courses, button_t_partners, button_motivation, button_working_method)





#Партнеры --- Рост (преподаватель)

teacher_kb_growth = types.InlineKeyboardMarkup(
    row_width = 1
)


button_growth_time_table = types.InlineKeyboardButton(
    'Расписание', url='https://robotmovavi.ru/')


teacher_kb_growth.add(button_grouth_olympiad, button_growth_time_table, button_grouth_courses)





#Партнеры --- Проскул (преподаватель)

teacher_kb_pro_school = types.InlineKeyboardMarkup(
    row_width = 1
)


button_pro_school_time_table = types.InlineKeyboardButton(
    'Расписание', url='https://robotmovavi.ru/')


teacher_kb_pro_school.add(button_pro_school_courses, button_pro_school_time_table)






#Партнеры --- 10ая гимназия (преподаватель)

teacher_kb_10th_gymnasium = types.InlineKeyboardMarkup(
    row_width = 1
)


button_10th_gymnasium_time_table = types.InlineKeyboardButton(
    'Расписание', url='https://robotmovavi.ru/')


teacher_kb_10th_gymnasium.add(button_10th_gymnasium_time_table)